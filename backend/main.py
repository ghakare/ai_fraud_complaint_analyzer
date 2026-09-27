from fastapi import FastAPI

from app.services.extraction import extract_entities
from app.services.analyzer import analyze_fraud
from app.services.patterns import detect_fraud_patterns
from app.ml.ml_model import predict_fraud
from app.services.hybrid_score import calculate_hybrid_score


app = FastAPI()


@app.post("/api/v1/fraud/analyze")
def analyze_complaint(data: dict):

    complaint = data["complaint"]

    entities = extract_entities(complaint)

    patterns=detect_fraud_patterns(complaint)

    analysis = analyze_fraud(entities,patterns, complaint)

    ml_result = predict_fraud(complaint)

    hybrid_score=calculate_hybrid_score(analysis['risk_score'], ml_result["fraud_probability"])

    return {
        "entities": entities,
        "patterns":patterns,
        "analysis": analysis,
        "ml_prediction": ml_result,
        "final_risk": hybrid_score

    }