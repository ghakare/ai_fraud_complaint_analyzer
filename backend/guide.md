import pypandoc

content = r"""AI FRAUD COMPLAINT ANALYZER
=============================

Purpose
-------
This document explains the complete project from start to end, including:
- Project setup
- FastAPI API
- Entity extraction
- Fraud pattern detection
- Rule-based risk analysis
- Machine Learning with TF-IDF + Logistic Regression
- Hybrid risk scoring
- Testing
- Important ML terminology and why each technology was selected

IMPORTANT:
This is a prototype/demo. The current ML model was trained on a very small synthetic dataset, so its ML confidence must NOT be treated as a real-world calibrated fraud probability.


1. PROJECT IDEA
===============

Problem:
People report cyber-fraud incidents using natural-language complaints.

Example:

"Someone called me saying he was from SBI. He said my account will be blocked and asked me to verify KYC and transfer 25000 to abc@ybl"

The system analyzes the complaint and identifies:
- Phone numbers
- UPI IDs
- Transaction amounts
- Organizations/banks
- Fraud-related patterns
- Rule-based risk
- ML fraud confidence
- Final hybrid risk score

Final architecture:

Complaint
   |
   +--> Entity Extraction
   |
   +--> Fraud Pattern Detection
   |
   +--> Rule-Based Risk Analysis
   |
   +--> ML Model
   |
   +--> Hybrid Risk Score
   |
   +--> Explainable JSON Response


2. PROJECT DIRECTORY
====================

Project:

manoj_sir_demo_1_fraud_ai/

Inside it:

backend/
|
+-- main.py
|
+-- app/
    |
    +-- services/
    |   +-- extraction.py
    |   +-- patterns.py
    |   +-- analyzer.py
    |   +-- hybrid_score.py
    |
    +-- ml/
        +-- dataset.py
        +-- train.py
        +-- ml_model.py

The exact project can later be expanded with tests, model files, a real dataset, logging, etc.


3. PYTHON VIRTUAL ENVIRONMENT
=============================

We created a virtual environment so that project dependencies are isolated from the system Python.

Command:

python3 -m venv .venv

Activate:

source .venv/bin/activate

Check Python:

which python

Expected result is a path similar to:

.../backend/.venv/bin/python

Why use a virtual environment?
--------------------------------
Different Python projects can require different package versions. A virtual environment prevents dependency conflicts.


4. INSTALL DEPENDENCIES
=======================

FastAPI:

pip install fastapi

Uvicorn:

pip install uvicorn

Scikit-learn:

pip install scikit-learn

The project currently uses:
- FastAPI for the API
- Uvicorn to run the API server
- scikit-learn for machine learning


5. FASTAPI BASICS
=================

Initial main.py:

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Fraud AI API is running"}

Important terminology:

FastAPI
-------
A Python web framework used to build APIs.

API
---
Application Programming Interface.

An API allows another application to communicate with our backend.

Endpoint
--------
A URL exposed by the API.

Example:

GET /

Decorator:
---------
@app.get("/")

The decorator registers the function below it as a GET endpoint.

GET
---
Normally used to retrieve information.

Example:

GET /complaints

POST
----
Normally used when the client sends data to the server for processing or creation.

Our project uses:

POST /api/v1/fraud/analyze

because the client sends a complaint to the backend for analysis.


6. RUNNING FASTAPI
==================

Run from the backend directory:

uvicorn main:app --reload

Why main:app?

main
----
Python module/file:

main.py

app
---
The FastAPI object:

app = FastAPI()

So:

uvicorn main:app

means:
"Find the app object inside main.py and run it."

--reload
-------
Automatically reloads the server when Python files change during development.

Swagger UI:

http://127.0.0.1:8000/docs

FastAPI automatically provides interactive API documentation.


7. COMPLAINT API
================

The main endpoint is:

POST /api/v1/fraud/analyze

Example request:

{
  "complaint": "Someone called me saying he was from SBI and asked me to transfer 25000 to abc@ybl"
}

The API processes this complaint through several services.


8. ENTITY EXTRACTION
====================

File:

app/services/extraction.py

Purpose:
Extract structured information from unstructured complaint text.

Example:

"I received a call from 9876543210. He said he was from SBI and asked me to transfer 25000 to abc@ybl"

Possible extracted entities:

phone:
9876543210

upi:
abc@ybl

amount:
25000

organisation:
SBI

Technology:
Python regular expressions using the re module.

Regular Expression / Regex
---------------------------
A pattern used to find specific text structures.

Example:

r"\b\d{10}\b"

This looks for a 10-digit number.

UPI pattern:

r"\b[\w.-]+@[\w.-]+\b"

This can identify values such as:

abc@ybl

Important limitation:
Regex is useful for structured patterns, but it is not a complete Natural Language Processing system. A production system could use better NER/NLP models and validation.


9. FRAUD PATTERN DETECTION
==========================

File:

app/services/patterns.py

Purpose:
Identify suspicious phrases and behaviors in the complaint.

Examples:

OTP request
Payment request
Urgency or account threat
Phone call mentioned
Verification request

Example complaint:

"SBI called me and said my account will be blocked. They asked me to verify KYC and transfer 25000."

Detected patterns can include:

Payment request
Urgency or account threat
Phone call mentioned
Verification request

This is a deterministic/rule-based layer.


10. RULE-BASED RISK ANALYSIS
============================

File:

app/services/analyzer.py

The analyzer gives weighted points for detected evidence.

Example:

UPI detected              -> points
Organization detected    -> points
Amount detected           -> points
Payment request           -> points
Urgency/account threat   -> points
Verification request      -> points

The points are added into a rule score.

Risk levels:

HIGH
MEDIUM
LOW

Why use rules?
---------------
Rules are:
- Easy to understand
- Easy to explain to a manager
- Deterministic
- Useful when known fraud indicators are present

Example explanation:

"UPI Id Detected"
"Transaction Amount Detected"
"Payment Request Detected"
"Urgency or Account Threat Detected"

This makes the system explainable.


11. MACHINE LEARNING PART
=========================

The ML files are:

app/ml/dataset.py
app/ml/train.py
app/ml/ml_model.py

The ML problem is:

Input:
Complaint text

Output:
Fraud or Normal

Labels:

1 = Fraud
0 = Normal


12. DATASET
===========

File:

app/ml/dataset.py

We initially created 12 synthetic examples:
- 6 fraud
- 6 normal

Fraud examples include concepts such as:
- OTP requests
- KYC/account threats
- Payment requests
- UPI transfers
- Fake bank calls
- Lottery/payment scams

Normal examples include:
- Bank balance checking
- Electricity bill payment
- Salary credit
- Grocery payment
- Passbook update
- Normal money transfer

IMPORTANT:
This dataset is only for demonstrating the ML pipeline. Twelve examples are not enough to build a production fraud model.

For production, a larger, representative and properly labelled dataset would be required.


13. WHAT IS MACHINE LEARNING?
=============================

Machine Learning is a method where an algorithm learns patterns from examples instead of relying only on manually written rules.

Traditional rule:

IF complaint contains OTP
THEN increase fraud score

ML approach:

Give the model many labelled examples.

Fraud examples -> label 1
Normal examples -> label 0

The model learns statistical relationships between text features and labels.


14. WHY TF-IDF?
===============

TF-IDF means:

Term Frequency - Inverse Document Frequency

It converts text into numerical features that an ML algorithm can process.

A machine learning model such as Logistic Regression cannot directly work with:

"Someone called me and asked for OTP"

It needs numerical input.

TF-IDF converts text into numbers representing the importance of words in the dataset.


15. TF = TERM FREQUENCY
=======================

Term Frequency measures how often a word occurs in a document.

If the word "OTP" occurs in a complaint, its frequency contributes to the representation of that complaint.


16. IDF = INVERSE DOCUMENT FREQUENCY
====================================

IDF reduces the importance of words that appear in many documents and gives more importance to words that are more distinctive.

A word that appears in almost every complaint is less useful for distinguishing complaints.

A word that appears in fewer documents may provide more information.

TF-IDF combines these ideas.

Conceptually:

TF-IDF = Term Frequency x Inverse Document Frequency


17. WHY TfidfVectorizer?
=======================

We used:

from sklearn.feature_extraction.text import TfidfVectorizer

TfidfVectorizer does two important things together:

1. Creates a vocabulary from raw text.
2. Converts the raw text directly into a TF-IDF numerical matrix.

Example:

complaints = [
    "Send OTP immediately",
    "I paid my electricity bill"
]

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(complaints)

Now X contains numerical TF-IDF features.


18. WHY NOT TfidfTransformer?
=============================

We initially discussed TfidfTransformer, but TfidfVectorizer is the correct choice for our current input.

TfidfVectorizer
---------------
Input:
RAW TEXT

Example:
"Send OTP immediately"

It performs:
Text -> tokenization/vocabulary -> TF-IDF features

TfidfTransformer
----------------
It expects numerical count/tf features that have already been created.

Typical pipeline:

CountVectorizer
      |
      v
Count matrix
      |
      v
TfidfTransformer
      |
      v
TF-IDF matrix

So:

TfidfVectorizer
---------------
Raw text -> TF-IDF

TfidfTransformer
----------------
Existing count/tf matrix -> TF-IDF

Because our dataset contains raw complaint strings, TfidfVectorizer is simpler and appropriate.

This distinction is important in an interview.


19. fit_transform()
===================

We used:

X = vectorizer.fit_transform(complaints)

fit:
Learn the vocabulary and IDF information from the training text.

transform:
Convert the text into numerical TF-IDF vectors.

fit_transform:
Perform both operations together.

Important:
fit should be performed on training data.

For unseen/test text, we use:

vectorizer.transform([test_complaint])

We do NOT fit again on test text.


20. LOGISTIC REGRESSION
=======================

We used:

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

model.fit(X, labels)

Despite the word "Regression", Logistic Regression is commonly used for classification.

Our classes are:

0 = NORMAL
1 = FRAUD

The model learns a relationship between the TF-IDF features and these labels.


21. WHAT DOES model.fit() MEAN?
===============================

This is the learning/training step.

X:
Numerical TF-IDF features.

labels:
Correct answers.

Example:

X + labels
    |
    v
model.fit()
    |
    v
Learned model

The model learns parameters that help distinguish fraud text from normal text.


22. WHAT IS CLASSIFICATION?
===========================

Classification means predicting a category/class.

Our classes are:

Class 0 -> NORMAL
Class 1 -> FRAUD

This is binary classification because there are two classes.


23. predict()
=============

We use:

prediction = model.predict(test_X)[0]

This gives the predicted class.

Example:

[1]

means:

FRAUD


24. predict_proba()
===================

We use:

probability = model.predict_proba(test_X)[0][1]

predict_proba gives the model's estimated class probabilities.

For example:

[0.35, 0.65]

means:

Normal = 35%
Fraud  = 65%

The second value [1] corresponds to class 1, which is FRAUD.

In our current example, the model returned approximately:

Fraud confidence = 0.63

or:

63%


25. IMPORTANT: CONFIDENCE VS REAL PROBABILITY
=============================================

Because the training dataset is extremely small and synthetic, we should not claim:

"There is a real 63% probability that this complaint is fraudulent."

Instead, for the demo, say:

"ML fraud confidence is 63% based on the current training model."

A production probability would require:
- Much larger data
- Representative data
- Proper train/validation/test splits
- Probability calibration
- Evaluation metrics
- Real-world validation


26. ml_model.py
==============

File:

app/ml/ml_model.py

Purpose:
Keep the trained vectorizer/model and expose a reusable function.

Function:

predict_fraud(complaint)

Flow:

Complaint text
    |
vectorizer.transform()
    |
TF-IDF features
    |
model.predict()
    |
FRAUD / NORMAL

and:

model.predict_proba()
    |
Fraud confidence


27. WHY DO WE HAVE train.py?
============================

train.py was used during development to verify that the ML model works.

It demonstrated:

1. Load dataset
2. Create TF-IDF vectorizer
3. Convert text to numerical features
4. Create Logistic Regression model
5. Train model
6. Test a complaint
7. Print prediction and probability

Later, reusable prediction logic was moved into ml_model.py.

This separation makes the project cleaner:

dataset.py
    |
    v
Training data

ml_model.py
    |
    v
Reusable trained model/prediction function

train.py
    |
    v
Development/testing script


28. HYBRID RISK SCORING
=======================

File:

app/services/hybrid_score.py

The project has two independent signals:

1. Rule-based score
2. ML fraud confidence

Example:

Rule score = 95

ML probability = 0.63

Convert ML probability to score:

0.63 x 100 = 63


29. HYBRID FORMULA
==================

For this prototype:

Final Score =
    (Rule Score x 0.70)
    +
    (ML Score x 0.30)

Example:

Rule Score = 95
ML Score = 63

Final:

(95 x 0.70) + (63 x 0.30)

= 66.5 + 18.9

= 85.4

Rounded:

85

Risk:

HIGH


30. WHY 70/30?
==============

The 70/30 weighting is a simple prototype choice.

We give more weight to explicit, explainable rule evidence because:
- The rules are transparent.
- The current ML dataset is very small.
- The rules directly identify known fraud indicators.

This is NOT a scientifically validated production weighting.

With a real dataset, weights should be validated using data and appropriate evaluation methods.


31. FINAL API FLOW
=================

main.py receives the complaint.

Step 1:
entities = extract_entities(complaint)

Step 2:
patterns = detect_fraud_patterns(complaint)

Step 3:
analysis = analyze_fraud(entities, patterns, complaint)

Step 4:
ml_result = predict_fraud(complaint)

Step 5:
hybrid_result = calculate_hybrid_score(
    analysis["risk_score"],
    ml_result["fraud_probability"]
)

Step 6:
Return all results as JSON.


32. EXAMPLE FINAL RESPONSE
==========================

Example:

{
  "entities": {
    "phone": [],
    "upi": [
      "abc@ybl"
    ],
    "amount": [
      "25000"
    ],
    "organisation": [
      "SBI"
    ]
  },

  "patterns": [
    "Payment request",
    "Urgency or account threat",
    "Phone call mentioned",
    "Verification request"
  ],

  "analysis": {
    "risk_score": 95,
    "risk_level": "HIGH",
    "reasons": [
      "UPI Id Detected",
      "Organisation Detected",
      "Transaction Amount Detected",
      "Payment Request Detected",
      "Urgency or Account Threat Detected",
      "Verification Request Detected"
    ]
  },

  "ml_prediction": {
    "prediction": "FRAUD",
    "fraud_probability": 0.63
  },

  "final_risk": {
    "final_score": 85,
    "risk_level": "HIGH",
    "rule_score": 95,
    "ml_score": 63
  }
}


33. WHAT EACH RESULT MEANS
==========================

entities
--------
Structured information found inside the complaint.

patterns
--------
Known suspicious language/behavior detected using rules.

analysis
--------
Explainable rule-based risk assessment.

ml_prediction
-------------
Machine learning prediction and current model confidence.

final_risk
----------
Hybrid result combining rule evidence and ML evidence.


34. API TESTING
===============

Start the server from backend:

uvicorn main:app --reload

Open:

http://127.0.0.1:8000/docs

Select:

POST /api/v1/fraud/analyze

Example request:

{
  "complaint": "Someone called me saying he was from SBI. He said my account will be blocked and asked me to verify KYC and transfer 25000 to abc@ybl"
}

Click Execute.

Swagger displays the JSON response.


35. PYTHONPATH ISSUE ENCOUNTERED
================================

While testing the ML script, this command caused:

python app/ml/train.py

and there was an import error involving the backend package.

The working command was:

PYTHONPATH=. python app/ml/train.py

Why?

The project was being executed from the backend directory, and app is inside that directory.

For example:

backend/
    app/
    main.py

Setting:

PYTHONPATH=.

tells Python to include the current backend directory when resolving imports.

This allowed:

from app.ml.dataset import complaints, labels

to work correctly.

This is mainly a development/import-path issue, not an ML issue.


36. COMPLETE TECHNOLOGY STACK
==============================

Python
------
Programming language.

FastAPI
--------
Backend API framework.

Uvicorn
-------
ASGI server used to run FastAPI.

Regex / re
----------
Used for simple entity extraction.

scikit-learn
------------
Machine learning library.

TfidfVectorizer
---------------
Converts raw complaint text into TF-IDF numerical features.

LogisticRegression
-------------------
Binary classification model used for Fraud vs Normal.

Swagger UI
----------
Interactive API testing/documentation automatically provided by FastAPI.


37. WHY THIS IS A HYBRID AI SYSTEM
==================================

It is hybrid because it combines:

Rule-based intelligence
+
Machine learning

Rules are good for:
- Known indicators
- Explainability
- Deterministic decisions

ML is useful for:
- Learning statistical patterns from examples
- Handling combinations of words/features
- Producing a learned prediction

Together:

Rules -> explainable evidence
ML -> learned text signal
Hybrid -> combined risk assessment


38. WHAT IS NOT YET PRODUCTION READY
====================================

This project is a prototype.

Important limitations:

1. Only a very small synthetic dataset is used.
2. No real fraud dataset is used.
3. No proper train/validation/test split has been implemented.
4. No cross-validation has been performed.
5. No precision, recall, F1-score or confusion matrix evaluation has been performed.
6. The hybrid 70/30 weighting is manually chosen for demonstration.
7. Regex entity extraction has limitations.
8. The ML probability is not calibrated for real-world fraud probability.
9. The model is not persisted to a model file yet.
10. There is no database, authentication or production monitoring.

These are appropriate future improvements rather than requirements for the current demo.


39. HOW TO EXPLAIN THE PROJECT TO A MANAGER
===========================================

Short explanation:

"I built a prototype AI-based fraud complaint analyzer using FastAPI and Python. The system accepts a natural-language complaint, extracts entities such as UPI IDs, transaction amounts and organizations, detects known fraud patterns, calculates an explainable rule-based risk score, and also uses a TF-IDF plus Logistic Regression model to estimate fraud confidence. Finally, I combine the rule score and ML signal into a simple hybrid risk score and return the result through a REST API."


40. IMPORTANT INTERVIEW QUESTIONS AND ANSWERS
==============================================

Q: Why FastAPI?
A:
"FastAPI provides a lightweight REST API layer with automatic Swagger documentation, which makes the AI service easy to test and integrate with other applications."

Q: Why Regex?
A:
"For the prototype, Regex is simple and effective for structured entities such as phone numbers, UPI IDs and amounts."

Q: Why TF-IDF?
A:
"TF-IDF converts raw text into numerical features based on word importance, allowing a traditional ML classifier to process complaint text."

Q: Why TfidfVectorizer instead of TfidfTransformer?
A:
"TfidfVectorizer works directly on raw text and combines vocabulary creation with TF-IDF transformation. TfidfTransformer expects an already-created numerical count or TF matrix."

Q: Why Logistic Regression?
A:
"It is a simple and effective classification algorithm for text features and can provide class probabilities, which are useful for our fraud confidence signal."

Q: Why not use an LLM?
A:
"For the first prototype I wanted a lightweight, explainable and locally testable ML pipeline. An LLM can be considered later for richer language understanding or explanation."

Q: Why combine rules and ML?
A:
"Rules provide transparent evidence, while ML provides a learned signal from historical examples. Combining them gives a more explainable hybrid prototype."

Q: Is the model production-ready?
A:
"No. The current model is a proof of concept trained on a small synthetic dataset. Production deployment would require a larger representative dataset, proper evaluation, calibration, security and monitoring."


41. FINAL PROJECT STATUS
========================

Completed prototype:

YES

Working components:

- FastAPI API
- Swagger testing
- Entity extraction
- Fraud pattern detection
- Rule-based scoring
- TF-IDF feature extraction
- Logistic Regression classification
- Fraud confidence
- Hybrid risk scoring
- Explainable reasons
- End-to-end JSON response

The project can currently be demonstrated through:

http://127.0.0.1:8000/docs

The next future improvements, if required, would be:
- Larger real/representative dataset
- Proper model evaluation
- Train/validation/test split
- Model persistence
- Better NLP/entity extraction
- Authentication and database
- Production deployment
- Optional Flutter frontend

For the current manager demonstration, the FastAPI Swagger interface is sufficient.
"""

output_path = "/mnt/data/AI_Fraud_Complaint_Analyzer_Project_Documentation.txt"
pypandoc.convert_text(content, 'plain', format='md', outputfile=output_path, extra_args=['--standalone'])
print(output_path)
