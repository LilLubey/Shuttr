import pandas as pd
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POST_PATH = os.path.join(BASE_DIR, "data", "posts.csv")

def create_post(username):
    while True:
        print("\n========================")
        print("       POST FORUM       ")
        print("========================")

        title = input("Judul       : ").strip()
        if not title:
            print("Judul tidak boleh kosong\n")
            continue

        content = input("Deskripsi   : ").strip()
        if not content:
            print("Deskripsi tidak boleh kosong\n")
            continue

        # Load / create dataframe
        if not os.path.exists(POST_PATH):
            df = pd.DataFrame(columns=["id", "username", "title", "content", "created_at"])
            new_id = 1
        else:
            df = pd.read_csv(POST_PATH)
            new_id = df["id"].max() + 1 if not df.empty else 1

        post = {
            "id": new_id,
            "username": username,
            "title": title,
            "content": content,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        df = pd.concat([df, pd.DataFrame([post])], ignore_index=True)
        df.to_csv(POST_PATH, index=False)

        print("\nPostingan berhasil dibuat")
        break

def list_posts():
    if not os.path.exists(POST_PATH):
        print("\n Belum ada postingan")
        return

    df = pd.read_csv(POST_PATH)

    if df.empty:
        print("\n Belum ada postingan")
        return

    print("\n========================")
    print("     DAFTAR POSTINGAN   ")
    print("========================")

    for _, row in df.iterrows():
        print(f"\n[{row['id']}] {row['title']}")
        print(f"Oleh   : {row['username']}")
        print(f"Isi    : {row['content']}")
        print(f"Waktu  : {row['created_at']}")
        print("-" * 30)

def delete_post(username):
    if not os.path.exists(POST_PATH):
        print("\n Tidak ada postingan")
        return

    df = pd.read_csv(POST_PATH)
    user_posts = df[df["username"] == username].reset_index(drop=True)

    if user_posts.empty:
        print("\n Kamu belum punya postingan")
        return

    print("\n========================")
    print("   HAPUS POSTINGAN      ")
    print("========================")

    for i, row in user_posts.iterrows():
        print(f"{i+1}. [{row['id']}] {row['title']}")

    choice = input("\nPilih nomor postingan (0 batal): ").strip()

    if choice == "0":
        return

    if not choice.isdigit():
        print(" Input harus angka")
        return

    choice = int(choice)

    if choice < 1 or choice > len(user_posts):
        print(" Nomor tidak valid")
        return

    post_id = user_posts.iloc[choice - 1]["id"]

    df = df[df["id"] != post_id]
    df.to_csv(POST_PATH, index=False)

    print(" Postingan berhasil dihapus")

