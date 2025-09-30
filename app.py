
from fastapi import FastAPI
import joblib
app = FastAPI()
model = joblib.load("fake_news_model.pkl")

@app.post("/predict")
def predict(news:str):
    pred = model.predict([news])[0]
    prob = model.predict_proba([news])[0].max()
    label = "Real" if pred ==1 else "Fake"
    return {"label": label, "confidence":float(prob)}
