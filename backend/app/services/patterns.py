import re


def detect_fraud_patterns(complaint: str):

    text = complaint.lower()

    patterns = []

    if re.search(r"\b(otp|one[- ]time password)\b", text):
        patterns.append("OTP request")

    if re.search(r"\b(transfer|send|pay|payment)\b", text):
        patterns.append("Payment request")

    if re.search(r"\b(blocked|suspended|urgent|immediately|expire|expired)\b", text):
        patterns.append("Urgency or account threat")

    if re.search(r"\b(call|called|calling)\b", text):
        patterns.append("Phone call mentioned")

    if re.search(r"\b(verify|verification|kyc)\b", text):
        patterns.append("Verification request")

    return patterns