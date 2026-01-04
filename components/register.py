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

        # 1️⃣ VALIDASI FIELD KOSONG (SPESIFIK)
        if not email:
            print(" Email tidak boleh kosong")
            continue
        if not username:
            print(" Username tidak boleh kosong")
            continue
        if not password:
            print(" Password tidak boleh kosong")
            continue

        # 2️⃣ VALIDASI FORMAT EMAIL
        if "@" not in email or "." not in email:
            print(" Format email tidak valid")
            continue

        # 3️⃣ VALIDASI PASSWORD
        if len(password) < 6:
            print(" Password minimal 6 karakter")
            continue

        # Load data
        if not os.path.exists(CREDENTIALS_PATH):
            df = pd.DataFrame(columns=["email", "username", "password"])
        else:
            df = pd.read_csv(CREDENTIALS_PATH)
            df = df.astype(str).apply(lambda col: col.str.strip())

        # 4️⃣ VALIDASI DUPLIKAT (SPESIFIK)
        if (df["email"] == email).any():
            print(" Email sudah terdaftar")
            continue
        if (df["username"] == username).any():
            print(" Username sudah terdaftar")
            continue

        # Simpan user
        new_user = pd.DataFrame(
            [[email, username, password]],
            columns=["email", "username", "password"]
        )

        df = pd.concat([df, new_user], ignore_index=True)
        df.to_csv(CREDENTIALS_PATH, index=False)

        print("\n✅ Registrasi berhasil! Silakan login.")
        break
