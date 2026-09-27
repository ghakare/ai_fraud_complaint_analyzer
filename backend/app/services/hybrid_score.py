def calculate_hybrid_score(rule_score, fraud_probability):

    ml_score = fraud_probability * 100

    final_score = (rule_score * 0.70) + (ml_score * 0.30)

    final_score = round(final_score)

    if final_score >= 70:
        risk_level = "HIGH"
    elif final_score >= 40:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"

    return {
        "final_score": final_score,
        "risk_level": risk_level,
        "rule_score": rule_score,
        "ml_score": round(ml_score)
    }