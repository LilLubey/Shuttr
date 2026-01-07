import pandas as pd
import os
from components.validators import is_valid_username, is_valid_password
from components.post import my_posts

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CREDENTIALS_PATH = os.path.join(BASE_DIR, "data", "credentials.csv")
POST_PATH = os.path.join(BASE_DIR, "data", "posts.csv")


def show_profile(username):
    while True:
        print("\n========================")
        print("        PROFIL          ")
        print("========================")
        print(f"Username saat ini : {username}\n")

        print("1. Ubah username")
        print("2. Ganti password")
        print("3. Lihat postingan saya")
        print("0. Kembali ke dashboard")

        choice = input("\nPilih menu: ").strip()

        if choice == "1":
            username = change_username(username)

        elif choice == "2":
            change_password(username)

        elif choice == "3":
            my_posts(username)   # 🔥 panggil fungsi dari post.py

        elif choice == "0":
            return username

        else:
            print("\n- Menu tidak valid")



def change_username(old_username):
    df = pd.read_csv(CREDENTIALS_PATH, dtype=str)
    df = df.apply(lambda col: col.str.strip())

    new_username = input("\nMasukkan username baru: ").strip()

    # VALIDASI
    valid, msg = is_valid_username(new_username)
    if not valid:
        print(f"- {msg}")
        return old_username

    if (df["username"] == new_username).any():
        print("- Username sudah digunakan")
        return old_username

    # UPDATE CREDENTIALS
    df.loc[df["username"] == old_username, "username"] = new_username
    df.to_csv(CREDENTIALS_PATH, index=False)

    # SINKRON KE POSTS
    if os.path.exists(POST_PATH):
        posts = pd.read_csv(POST_PATH, dtype=str)
        posts.loc[posts["username"] == old_username, "username"] = new_username
        posts.to_csv(POST_PATH, index=False)

    print("\n- Username berhasil diubah")
    return new_username


def change_password(username):
    new_password = input("\nMasukkan password baru: ").strip()

    valid, msg = is_valid_password(new_password)
    if not valid:
        print(f"- {msg}")
        return

    df = pd.read_csv(CREDENTIALS_PATH, dtype=str)
    df.loc[df["username"] == username, "password"] = new_password
    df.to_csv(CREDENTIALS_PATH, index=False)

    print("\n- Password berhasil diubah")
