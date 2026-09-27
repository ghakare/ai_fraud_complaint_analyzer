from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from app.ml.dataset import complaints,labels

vectorize = TfidfVectorizer()
X =vectorize.fit_transform(complaints)

model = LogisticRegression()
model.fit(X,labels)

def predict_fraud(complaints:str):
    test_X=vectorize.transform([complaints])
    prediction = model.predict(test_X)
    probablity = model.predict_proba(test_X)[0][1]

    return {
          "prediction": "FRAUD" if prediction == 1 else "NORMAL",
          "fraud_probability": round(float(probablity), 2)
    }
