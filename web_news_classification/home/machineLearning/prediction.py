import requests
from bs4 import BeautifulSoup
import pickle
import numpy as np
from pathlib import Path

## pip install tensorflow
## pip install scikit-learn

# get text from url
def get_text_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    content = soup.get_text()
    title = soup.find('h1').text.strip()
    return title, content
    
# preprocess_text
def preprocess_text(text):
    text_tfidf = vectorizer.transform([text])
    return text_tfidf.toarray()

# load model
with open(Path(__file__).with_name("model.pkl"), "rb") as f:
    model = pickle.load(f)

# load trained TfidfVectorizer
with open(Path(__file__).with_name("vectorizer.pkl"), "rb") as f:
    vectorizer = pickle.load(f)

# load LabelEncoder
with open(Path(__file__).with_name("label_encoder.pkl"), "rb") as f:
    label_encoder = pickle.load(f)

# predict news's category
def predict(url):
    
    title, content = get_text_from_url(url)

    preprocessed_content = preprocess_text(content)

    prediction = model.predict(preprocessed_content)
    predicted_class = np.argmax(prediction)

    predicted_label = label_encoder.inverse_transform([predicted_class])
    
    return title, predicted_label[0], content


