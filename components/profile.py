import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CREDENTIALS_PATH = os.path.join(BASE_DIR, "data", "credentials.csv")

def show_profile(username):
    while True:
        print("\n========================")
        print("        PROFIL          ")
        print("========================")
        print(f"Username saat ini : {username}\n")

        print("1. Ubah username")
        print("0. Kembali ke dashboard")

        choice = input("\nPilih menu: ").strip()

        if choice == "1":
            username = change_username(username)
        elif choice == "0":
            return username
        else:
            print("\n❌ Menu tidak valid")

def change_username(old_username):
    df = pd.read_csv(CREDENTIALS_PATH)

    new_username = input("\nMasukkan username baru: ").strip()

    if not new_username:
        print("❌ Username tidak boleh kosong")
        return old_username

    if (df["username"] == new_username).any():
        print("❌ Username sudah digunakan")
        return old_username

    df.loc[df["username"] == old_username, "username"] = new_username
    df.to_csv(CREDENTIALS_PATH, index=False)

    print("\n✅ Username berhasil diubah")
    return new_username
