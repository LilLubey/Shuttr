import pandas as pd
import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CREDENTIALS_PATH = os.path.join(BASE_DIR, "data", "credentials.csv")

ALLOWED_DOMAINS = [
    "gmail.com",
    "outlook.com",
    "yahoo.com",
    "student.upi.edu"
]


def is_valid_email(email):
    errors = []

    if any(c.isupper() for c in email):
        errors.append("tidak boleh ada huruf kapital")

    if email.count("@") != 1:
        errors.append("hanya boleh 1 @")
    else:
        local, domain = email.split("@")

        if not re.match(r"^[a-z0-9._%-]+$", local):
            errors.append("format sebelum '@' tidak valid")

        if domain not in ALLOWED_DOMAINS:
            errors.append("domain harus gmail.com / outlook.com / yahoo.com / student.upi.edu")

    if errors:
        return False, errors

    return True, []


def is_valid_password(pw):
    errors = []

    if len(pw) < 6:
        errors.append("minimal 6 karakter")

    if not re.search(r"[A-Z]", pw):
        errors.append("harus ada huruf besar")

    if not re.search(r"[0-9]", pw):
        errors.append("harus ada angka")

    if not re.search(r"[!@#$%^&*()_+=\[\]{};:,.<>?/\-]", pw):
        errors.append("harus ada simbol")

    if errors:
        return False, errors

    return True, []


def register():
    while True:
        print("\n========================")
        print("       REGISTRASI       ")
        print("========================")
        print("Ketik 0 untuk kembali ke menu LOGIN\n")

        email = input("Email    : ").strip()

        # user ingin login
        if email == "0":
            print("\n➡ Kembali ke menu login...")
            return  # biarkan main menu memanggil login()

        username = input("Username : ").strip()
        password = input("Password : ").strip()

        if not email:
            print("- Email tidak boleh kosong")
            continue
        if not username:
            print("- Username tidak boleh kosong")
            continue
        if not password:
            print("- Password tidak boleh kosong")
            continue

        valid_email, email_errors = is_valid_email(email)
        if not valid_email:
            print("\nEmail tidak valid:")
            for e in email_errors:
                print(f" - {e}")
            continue

        if not re.match(r"^[A-Za-z0-9_]+$", username):
            print("- Username tidak boleh mengandung simbol")
            continue

        valid_pw, pw_errors = is_valid_password(password)
        if not valid_pw:
            print("\nPassword tidak valid:")
            for e in pw_errors:
                print(f" - {e}")
            continue

        if not os.path.exists(CREDENTIALS_PATH):
            df = pd.DataFrame(columns=["email", "username", "password"])
        else:
            df = pd.read_csv(CREDENTIALS_PATH, dtype=str)

        if (df["email"] == email).any():
            print("- Email sudah terdaftar")
            continue

        if (df["username"] == username).any():
            print("- Username sudah digunakan")
            continue

        new = pd.DataFrame(
            [[email, username, password]],
            columns=["email", "username", "password"]
        )

        df = pd.concat([df, new], ignore_index=True)
        df.to_csv(CREDENTIALS_PATH, index=False)

        print("\n✅ Registrasi berhasil! Silakan login.")
        return  # selesai, kembali ke menu login
