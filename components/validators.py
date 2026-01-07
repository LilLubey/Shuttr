import re

ALLOWED_DOMAINS = ["gmail.com", "outlook.com", "yahoo.com", "student.upi.edu"]

def is_valid_email(email):
    if not email:
        return False, "Email tidak boleh kosong"

    if email != email.lower():
        return False, "Email tidak boleh huruf kapital"

    if not email.replace("@", "").replace(".", "").isalnum():
        return False, "Email tidak boleh mengandung simbol"

    if "@" not in email:
        return False, "Format email tidak valid"

    domain = email.split("@")[-1]

    if domain not in ALLOWED_DOMAINS and not domain.startswith("student."):
        return False, "Domain email tidak diizinkan"

    return True, ""

def is_valid_username(username):
    if not username:
        return False, "Username tidak boleh kosong"

    if not username.isalnum():
        return False, "Username tidak boleh mengandung simbol"

    return True, ""

def is_valid_password(password):
    if len(password) < 6:
        return False, "Password minimal 6 karakter"

    if not re.search(r"[A-Z]", password):
        return False, "Password harus mengandung huruf kapital"

    if not re.search(r"[0-9]", password):
        return False, "Password harus mengandung angka"

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password harus mengandung simbol"

    return True, ""
