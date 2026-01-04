from components.post import create_post
from components.profile import show_profile
from components.search import search_post
from components.post import list_posts
from components.post import delete_post

def header(title):
    print("\n" + "=" * 30)
    print(title.center(30))
    print("=" * 30)

def dashboard(username):
    while True:
        header("MENU DASHBOARD")
        print(f"Login sebagai: {username}\n")

        print("1. Post forum")
        print("2. Lihat postingan")
        print("3. Cari postingan")
        print("4. Hapus postingan saya")
        print("5. Profil")
        print("0. Logout")

        choice = input("\nPilih menu: ").strip()

        if choice == "1":
            create_post(username)

        elif choice == "2":
            list_posts()

        elif choice == "3":
            search_post()  

        elif choice == "4":
            delete_post(username)

        elif choice == "5":
            username = show_profile(username)

        elif choice == "0":
            print("\n Logout berhasil")
            break

        else:
            print("\n Menu tidak valid")
