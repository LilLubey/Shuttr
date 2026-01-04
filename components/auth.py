import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CREDENTIALS_PATH = os.path.join(BASE_DIR, "data", "credentials.csv")

def login():
    if not os.path.exists(CREDENTIALS_PATH) or os.path.getsize(CREDENTIALS_PATH) == 0:
        print("❌ Belum ada user terdaftar")
        return None

    df = pd.read_csv(CREDENTIALS_PATH, dtype=str)
    df.columns = df.columns.str.strip()
    df = df.apply(lambda col: col.map(lambda x: x.strip() if isinstance(x, str) else x))

    print("\n========================")
    print("         LOGIN          ")
    print("========================")

    email = input("Email (opsional)    : ").strip()
    username = input("Username (opsional) : ").strip()
    password = input("Password            : ").strip()

    # 1️⃣ VALIDASI INPUT
    if not password:
        print("❌ Password wajib diisi")
        return None

    if not email and not username:
        print("❌ Isi email atau username")
        return None

    # 2️⃣ LOGIN DENGAN EMAIL
    if email:
        match = df[
            (df["email"] == email) &
            (df["password"] == password)
        ]

        if not match.empty:
            print("\n✅ Login berhasil")
            return match.iloc[0]["username"]
        else:
            print("\n❌ Email atau password salah")
            return None

    # 3️⃣ LOGIN DENGAN USERNAME
    if username:
        match = df[
            (df["username"] == username) &
            (df["password"] == password)
        ]

        if not match.empty:
            print("\n✅ Login berhasil")
            return username
        else:
            print("\n❌ Username atau password salah")
            return None

