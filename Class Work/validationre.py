import re
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))
def validate_phone_number(phone):
    pattern = r'^\+?[0-9]{10,15}$'
    return bool(re.match(pattern, phone))
def validate_password(password):
    pattern = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'
    return bool(re.match(pattern, password))
def validate_date(date_text):
    pattern = r'^\d{4}-\d{2}-\d{2}$'
    return bool(re.match(pattern, date_text))
validate_email("manikantaramkumar760@gmail.com")
validate_phone_number("+919347945897")
validate_password("Welcome123$")
validate_date("2003-12-10")
print("Email valid:",validate_email("manikantaramkumar760@gmail.com"))
print("Phone valid:",validate_phone_number("+919347945897"))
print("Password valid:",validate_password("Welcome123$"))
print("Date valid:",validate_date("2003-12-10"))
print("Email valid:",validate_email("invalid-email"))
print("Phone valid:",validate_phone_number("12345"))