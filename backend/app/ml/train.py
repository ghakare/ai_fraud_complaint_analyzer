from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from app.ml.dataset import complaints,labels
'''
TfidfVectorizer -  converts complaints text into numerical feasture

LogisticRegression - learn Fraud(1) vs Normal (0)

complaints, slabels - loads the training examples we just created.

''' 
vectorizer = TfidfVectorizer()

X= vectorizer.fit_transform(complaints)

 
model = LogisticRegression()
model.fit(X,labels)

test_complaint="Someone called me and asked me to send OTP imedietly"

test_X= vectorizer.transform([test_complaint])
prediction =model.predict(test_X)
probablity= model.predict_proba(test_X)
print("Prediction:",prediction)
print("Probablity:",probablity)
