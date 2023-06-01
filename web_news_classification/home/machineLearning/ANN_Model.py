import spacy
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from keras.wrappers.scikit_learn import KerasClassifier
from keras import regularizers
import pickle
from gensim import corpora
from gensim.models import LdaModel
from home.models import Newsarticles, Categories

nlp = spacy.load("en_core_web_sm")

# preprocessing new content with spacy
def preprocess_text(text):
    text = text.lower()
    doc = nlp(text)
    lemmas = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    return lemmas

# 读取数据集
# data = pd.read_csv("training.csv", header=0, usecols=[6, 3], encoding="utf-8")

# get all news articles
articles = Newsarticles.objects.all()

# convert to DataFrame
data = pd.DataFrame.from_records([
    {'Content': article.content, 'CategoryName': article.categoryid.categoryname}
    for article in articles
])

# 提取摘要和标签
X = data["Content"]
y = data["CategoryName"]

# 处理NaN值
X = X.fillna(" ")

# 文本预处理
X = X.apply(preprocess_text)

# 建立字典
dictionary = corpora.Dictionary(X)

# 建立corpus
corpus = [dictionary.doc2bow(text) for text in X]

# 使用LDA模型
lda_model = LdaModel(corpus=corpus, id2word=dictionary, num_topics=10)

# 提取主题特征
X_topics = np.zeros((len(corpus), 10))  # 初始化一个全零矩阵
for i, doc in enumerate(corpus):
    topics = lda_model.get_document_topics(doc, minimum_probability=0)
    for topic_id, prob in topics:
        X_topics[i, topic_id] = prob

# 计算TF-IDF特征向量
vectorizer = TfidfVectorizer()
X_tfidf = vectorizer.fit_transform([' '.join(text) for text in X])

# 将TF-IDF特征向量转换为NumPy数组
X_tfidf = X_tfidf.toarray()

# 将TF-IDF特征和主题特征拼接
X_combined = np.hstack((X_tfidf, X_topics))

# 将标签编码为整数
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X_combined, y, test_size=0.3, random_state=123)

def create_model():
    model = Sequential()
    model.add(Dense(64, activation="relu", input_shape=(X_combined.shape[1],)))
    model.add(Dense(32, activation="relu", kernel_regularizer=regularizers.l1_l2(l1=0.001, l2=0.001)))
    model.add(Dense(len(set(y)), activation="softmax"))
    model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
    return model

model = KerasClassifier(build_fn=create_model, epochs=10, batch_size=32, verbose=0)

scores = cross_val_score(model, X_combined, y, cv=5)

# 训练模型
model = create_model()
history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, batch_size=32)

# 输出训练和测试准确率
train_acc = history.history['accuracy'][-1]
test_acc = history.history['val_accuracy'][-1]
print(f"Train accuracy: {train_acc*100:.2f}%")
print(f"Test accuracy: {test_acc*100:.2f}%")
print("Cross-validation accuracy: %.2f%% (+/- %.2f%%)" % (np.mean(scores)*100, np.std(scores)*100))

# 保存模型为pickle文件
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

# 保存训练过的TfidfVectorizer
with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

# 保存LabelEncoder
with open("label_encoder.pkl", "wb") as f:
    pickle.dump(label_encoder, f)
