import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CREDENTIALS_PATH = os.path.join(BASE_DIR, "data", "credentials.csv")

def login():
    if not os.path.exists(CREDENTIALS_PATH) or os.path.getsize(CREDENTIALS_PATH) == 0:
        print("❌ Belum ada user terdaftar")
        return None

    df = pd.read_csv(CREDENTIALS_PATH)
    df = df.astype(str).apply(lambda col: col.str.strip())

    print("\n=== LOGIN ===")
    email = input("Email    : ").strip()
    username = input("Username : ").strip()
    password = input("Password : ").strip()

    match = df[
        (df["email"] == email) &
        (df["username"] == username) &
        (df["password"] == password)
    ]

    if not match.empty:
        print("\n✅ Login berhasil")
        return username
    else:
        print("\n❌ Login gagal")
        return None
