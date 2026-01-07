import pandas as pd
import os
import re
import getpass

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CREDENTIALS_PATH = os.path.join(BASE_DIR, "data", "credentials.csv")

ALLOWED_DOMAINS = [
    "@gmail.com",
    "@outlook.com",
    "@yahoo.com",
    "@student.upi.edu"
]

def is_valid_email(email):
    # tidak boleh kapital
    if any(c.isupper() for c in email):
        return False

    # harus tepat satu @
    if email.count("@") != 1:
        return False

    # karakter hanya huruf, angka, ., _
    if not re.match(r"^[a-z0-9._@]+$", email):
        return False

    # domain harus sesuai list
    if not any(email.endswith(domain) for domain in ALLOWED_DOMAINS):
        return False

    return True


def is_valid_password(pw):
    if len(pw) < 6:
        return False
    if not re.search(r"[A-Z]", pw):
        return False
    if not re.search(r"[0-9]", pw):
        return False
    if not re.search(r"[!@#$%^&*()_\-+=\[{\]};:,.<>?/]", pw):
        return False
    return True


def login():
    # cek user file
    if not os.path.exists(CREDENTIALS_PATH) or os.path.getsize(CREDENTIALS_PATH) == 0:
        print("- Belum ada user terdaftar")
        return None

    df = pd.read_csv(CREDENTIALS_PATH, dtype=str)
    df = df.apply(lambda col: col.map(lambda x: x.strip() if isinstance(x, str) else x))

    print("\n========================")
    print("         LOGIN          ")
    print("========================")

    identity = input("Email/Username : ").strip()

    if not identity:
        print("- Email atau username wajib diisi")
        return None

    # pilihan apakah password disembunyikan
    mode = input("Sembunyikan password? (y/n): ").lower().strip()

    if mode == "y":
        password = getpass.getpass("Password       : ")
    else:
        password = input("Password       : ")

    if not password:
        print("- Password wajib diisi")
        return None

    # validasi kekuatan password
    if not is_valid_password(password):
        print("- Password salah")
        return None

    # jika yang dimasukkan email → validasi emailnya
    if "@" in identity:
        if not is_valid_email(identity):
            print("- Format email tidak valid")
            return None

    # cocokkan email ATAU username
    match = df[
        (
            (df["email"] == identity) |
            (df["username"] == identity)
        ) &
        (df["password"] == password)
    ]

    if match.empty:
        print("- Email/Username atau password salah")
        return None

    print("\n- Login berhasil")
    return match.iloc[0]["username"]
