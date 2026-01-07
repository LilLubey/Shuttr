import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POST_PATH = os.path.join(BASE_DIR, "data", "posts.csv")

def search_post():
    if not os.path.exists(POST_PATH):
        print("\n- Belum ada postingan")
        return

    keyword = input("\nCari kata kunci: ").strip().lower()

    if not keyword:
        print("- Kata kunci tidak boleh kosong")
        return

    df = pd.read_csv(POST_PATH)

    results = df[
        df["title"].str.lower().str.contains(keyword) |
        df["content"].str.lower().str.contains(keyword)
    ]

    if results.empty:
        print("\n- Postingan tidak ditemukan")
        return

    print("\n========================")
    print("   HASIL PENCARIAN      ")
    print("========================")

    for _, row in results.iterrows():
        print(f"\n[{row['id']}] {row['title']}")
        print(f"Oleh   : {row['username']}")
        print(f"Isi    : {row['content']}")
        print(f"Waktu  : {row['created_at']}")
        print("-" * 30)
