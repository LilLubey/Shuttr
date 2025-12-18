import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CREDENTIALS_PATH = os.path.join(BASE_DIR, "data", "credentials.csv")

def register():
    while True:
        print("\n========================")
        print("       REGISTRASI       ")
        print("========================")

        email = input("Email    : ").strip()
        username = input("Username : ").strip()
        password = input("Password : ").strip()

        # 1️⃣ VALIDASI FIELD KOSONG
        if not email or not username or not password:
            print("\n❌ Semua field WAJIB diisi.\n")
            continue

        # 2️⃣ VALIDASI FORMAT EMAIL
        if "@" not in email or "." not in email:
            print("\n❌ Format email tidak valid.\n")
            continue

        # 3️⃣ VALIDASI PANJANG PASSWORD
        if len(password) < 6:
            print("\n❌ Password minimal 6 karakter.\n")
            continue

        # Load data
        if not os.path.exists(CREDENTIALS_PATH):
            df = pd.DataFrame(columns=["email", "username", "password"])
        else:
            df = pd.read_csv(CREDENTIALS_PATH)
            df = df.astype(str).apply(lambda col: col.str.strip())

        # 4️⃣ VALIDASI DUPLIKAT
        if ((df["email"] == email) | (df["username"] == username)).any():
            print("\n❌ Email atau username sudah terdaftar.\n")
            continue

        # Simpan user baru
        new_user = pd.DataFrame(
            [[email, username, password]],
            columns=["email", "username", "password"]
        )

        df = pd.concat([df, new_user], ignore_index=True)
        df.to_csv(CREDENTIALS_PATH, index=False)

        print("\n✅ Registrasi berhasil! Silakan login.")
        break
