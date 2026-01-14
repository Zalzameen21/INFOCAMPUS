def validate_email(email):
    return "@" in email and "." in email

def validate_phone(phone):
    return phone.isdigit() and len(phone) == 10

def validate_name(name):
    return name.isalpha()
