import re

def validate_email(email):
    return re.match(r'^\S+@\S+\.\S+$', email) is not None

def validate_phone(phone):
    return re.match(r'^\d{10}$', phone) is not None

def validate_name(name):
    return name.isalpha()

def sanitize_input(text):
    return text.strip()