# Fungsi untuk menampilkan dashboard
def show_dashboard(user_data):
    print("="*40)
    print(f"Dashboard User: {user_data['username']}")
    print("="*40)
    print(f"Total Postingan : {len(user_data['posts'])}")
    print(f"Total Komentar  : {user_data['total_comment']}\n")

    print("Post Terbaru:")
    for post in user_data['posts'][-5:]:  # menampilkan 5 post terbaru
        print(f"- {post}")
    
    print("="*40)

# Inisialisasi data user
input_username = input("Masukkan nama user: ")
user_dashboard = {
    "username": input_username,
    "total_comment": 34,
    "posts": []  # list untuk menyimpan postingan
}

# Input postingan baru
while True:
    new_post = input("Masukkan judul postingan baru (ketik 'selesai' untuk berhenti): ")
    if new_post.lower() == "selesai":
        break
    user_dashboard['posts'].append(new_post)

# Tampilkan dashboard sesuai input user
show_dashboard(user_dashboard)