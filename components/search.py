import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POST_PATH = os.path.join(BASE_DIR, "data", "posts.csv")

def search_post():
    keyword = input("\nCari postingan : ").strip().lower()

    if not os.path.exists(POST_PATH):
        print("\n⚠️ Belum ada postingan")
        return

    df = pd.read_csv(POST_PATH)

    results = df[df["content"].str.lower().str.contains(keyword)]

    if results.empty:
        print("\n❌ Postingan tidak ditemukan")
        return

    print("\n--- HASIL PENCARIAN ---")
    for _, row in results.iterrows():
        print(f"\n@{row['username']}")
        print(row['content'])
