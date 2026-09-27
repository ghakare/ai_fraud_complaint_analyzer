import re


def extract_entities(complaint: str):

    phone_numbers = re.findall(r"\b\d{10}\b", complaint)

    upi_ids = re.findall(r"\b[\w.-]+@[\w.-]+\b", complaint)

    amount = re.findall(r"(?:₹\s*|\b(?:rs|inr)\s*)\d+(?:,\d+)*(?:\.\d+)?|\b\d{1,7}\b",complaint,re.IGNORECASE)
    organisation=re.findall(r"\b(?:SBI|ICICI|Axix bank|bank of baroda|paytm)\b",complaint,re.IGNORECASE)
    return {
        "phone": phone_numbers,
        "upi": upi_ids,
        "amount": amount,
        "organisation":organisation
    }