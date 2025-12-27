import csv

def upload_post(username):
    print("\n=== Upload Postingan ===")

    judul = input("Judul Postingan : ")
    isi = input("Isi Postingan   : ")

    with open("data/posts.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, judul, isi])

    print("\n✅ Postingan berhasil diupload")
