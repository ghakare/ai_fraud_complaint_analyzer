def analyze_fraud(entities, patterns, complaint):

    risk_score = 0
    reasons = []

    # Entity-based risk
    if entities["phone"]:
        risk_score += 15
        reasons.append("Phone Number Detected")

    if entities["upi"]:
        risk_score += 20
        reasons.append("UPI Id Detected")

    if entities["organisation"]:
        risk_score += 20
        reasons.append("Organisation Detected")

    if entities["amount"]:
        risk_score += 15
        reasons.append("Transaction Amount Detected")

    # Pattern-based risk
    if "OTP request" in patterns:
        risk_score += 25
        reasons.append("OTP Request Detected")

    if "Payment request" in patterns:
        risk_score += 15
        reasons.append("Payment Request Detected")

    if "Urgency or account threat" in patterns:
        risk_score += 15
        reasons.append("Urgency or Account Threat Detected")

    if "Verification request" in patterns:
        risk_score += 10
        reasons.append("Verification Request Detected")

    if risk_score >= 70:
        risk_level = "HIGH"
    elif risk_score >= 40:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"

    return {
        "risk_score": risk_score,
        "risk_level": risk_level,
        "reasons": reasons
    }