# Fungsi untuk menampilkan dashboard
def tampilan_dashboard(data_user):
    print("="*40)
    print(f"Dashboard : {data_user['username']}")
    print("="*40)
    print(f"Total postingan : {len(data_user['posts'])}")
    print(f"Total komentar  : {data_user['total_comment']}\n")

    print("Postingan terbaru:")
    for post in data_user['posts'][-5:]:  # menampilkan 5 postingan terbaru
        print(f"- {post}")
    
    print("="*40)

# input data user
input_username = input("Masukkan nama user: ")
user_dashboard = {
    "username": input_username,
    "total_comment": 34,
    "posts": []  # list untuk menyimpan postingan
}

# Input postingan baru
while True:
    postingan = input("masukkan judul postingan baru dan ketik 'selesai' untuk berhenti: ")
    if postingan.lower() == "selesai":
        break
    user_dashboard['postingan'].append(postingan)

# Tampilkan dashboard sesuai input user
tampilan_dashboard(user_dashboard) 