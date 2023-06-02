import requests
from bs4 import BeautifulSoup
import pickle
import numpy as np
from pathlib import Path

## pip install tensorflow
## pip install scikit-learn

# 从URL获取文本内容
def get_text_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    content = soup.get_text()
    title = soup.find('h1').text.strip()
    return title, content
    
# 预处理文本内容
def preprocess_text(text):
    text_tfidf = vectorizer.transform([text])
    return text_tfidf.toarray()

# 加载模型
with open(Path(__file__).with_name("model.pkl"), "rb") as f:
    model = pickle.load(f)

# 加载训练过的TfidfVectorizer
with open(Path(__file__).with_name("vectorizer.pkl"), "rb") as f:
    vectorizer = pickle.load(f)

# 加载LabelEncoder
with open(Path(__file__).with_name("label_encoder.pkl"), "rb") as f:
    label_encoder = pickle.load(f)

# 获取要预测的URL的内容
# content = get_text_from_url(url)

# # 预处理内容
# preprocessed_content = preprocess_text(content)

# # 使用模型进行预测
# prediction = model.predict(preprocessed_content)
# predicted_class = np.argmax(prediction)

# # 解码预测的类别
# predicted_label = label_encoder.inverse_transform([predicted_class])

# print(f"Predicted category: {predicted_label[0]}")

def predict(url):
    
    title, content = get_text_from_url(url)

    preprocessed_content = preprocess_text(content)

    prediction = model.predict(preprocessed_content)
    predicted_class = np.argmax(prediction)

    predicted_label = label_encoder.inverse_transform([predicted_class])
    
    return title, predicted_label[0], content


