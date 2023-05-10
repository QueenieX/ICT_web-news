import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
import pickle

# 读取数据集
data = pd.read_csv("news_dataset.csv", header=0, usecols=[2, 3], encoding="utf-8")

# 提取摘要和标签
X = data["Content"]
y = data["Category"]

# 处理NaN值
X = X.fillna(" ")

# 计算TF-IDF特征向量
vectorizer = TfidfVectorizer()
X_tfidf = vectorizer.fit_transform(X)

# 将TF-IDF特征向量转换为NumPy数组
X_tfidf = X_tfidf.toarray()

# 将标签编码为整数
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.3, random_state=123)

# 构建神经网络模型
def create_model():
    model = Sequential()
    model.add(Dense(64, activation="relu", input_shape=(X_tfidf.shape[1],)))
    model.add(Dense(32, activation="relu"))
    model.add(Dense(len(set(y)), activation="softmax"))
    model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
    return model

# 训练模型
model = create_model()
history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, batch_size=32)

# 输出训练和测试准确率
train_acc = history.history['accuracy'][-1]
test_acc = history.history['val_accuracy'][-1]
print(f"Train accuracy: {train_acc*100:.2f}%")
print(f"Test accuracy: {test_acc*100:.2f}%")

# 保存模型为pickle文件
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

# 保存训练过的TfidfVectorizer
with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

# 保存LabelEncoder
with open("label_encoder.pkl", "wb") as f:
    pickle.dump(label_encoder, f)
