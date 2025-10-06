# 📊 Fake News Detection with Machine Learning

## Project Overview
This project builds a **machine learning model** to classify articles as **Fake**
or **Real.**
It combines **exploratory data analysis (EDA)**, **text preprocessing**, and
**ML algorithms** to detect misleading content.
Finally, the trained model is deployed with **FastAPI** for easy use as an API.
---

## Features
- Exploratory Data Analysis (EDA) with word distributions and text length stats.
- Text preprocessing: cleaning, stopword removal, lemmatization.
- Feature extraction with **TF=IDF Vectorizer**.
- Model training with **Naive Bayes and Logistic Regression**.
- Explainability with **SHAP and model coefficients**.
- REST API deployment with **FastAPI**.

---

## Dataset
The dataset used (from https://www.kaggle.com/datasets/saurabhshahane/fake-news-classification)
contains lebeled news articles:
- 1 == Real News
- 0 == Fake News

---

## Tech Stack
- Python 3
- FastAPI (API framework)
- Uvicorn (ASGI server)
- Scikit-learn (ML models and TF-IDF)
- Pandas / Numpy (data handling)
- Matplotlib / Seaborn (visualization)
- NLTK / SpaCy (NLP preprocessing)
- SHAP (model explainability)

---
## Results
- **Logistic Regression** achieved better performance on text data than Logistic
Regression.
- F1 scores and accuracy were evaluated with **cross-validation**.
- Top indicative words for Fake vs Real were extracted from the trained model.

---


## How to Run
1. Clone this repository:
   '''bash
   git clone https://github.com/illostephanie4/Fake_news_detection.git
   cd Fake_news_detection
   '''

2. Install dependencies:
   '''bash
   pip install -r requirements.txt
   '''

3. Run API:
   '''bash
   uvicorn app:app --reload
   '''

4. Open http://127.0.0.1:8000/docs using the interactive UI to send news text
and get predictions

---

## Next Steps
- Expand dataset with more sources.
- Try deep learning models (e.g., LSTM, BERT)
- Deploy on cloud (Heroku, AWS, or Render)
- Build a simple frontend UI

---

## License
This project is licensed under the MIT License.

---

## Author
**Stephanie** - Data Science Enthusiast.
