import pandas as pd
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POST_PATH = os.path.join(BASE_DIR, "data", "posts.csv")

def create_post(username):
    print("\n========================")
    print("       POST FORUM       ")
    print("========================")

    content = input("Tulis postingan:\n> ").strip()

    if not content:
        print("\n❌ Postingan tidak boleh kosong")
        return

    post = {
        "username": username,
        "content": content,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    if not os.path.exists(POST_PATH):
        df = pd.DataFrame(columns=post.keys())
    else:
        df = pd.read_csv(POST_PATH)

    df = pd.concat([df, pd.DataFrame([post])], ignore_index=True)
    df.to_csv(POST_PATH, index=False)

    print("\n✅ Postingan berhasil dibuat")
