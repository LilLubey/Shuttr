from components.post import create_post
from components.profile import show_profile
from components.search import search_post
from components.profile import show_profile

def header(title):
    print("\n" + "=" * 30)
    print(title.center(30))
    print("=" * 30)

def dashboard(username):
    while True:
        header("MENU DASHBOARD")
        print(f"Login sebagai: {username}\n")

        print("1. Post forum")
        print("2. Profil")
        print("3. Cari postingan")
        print("0. Logout")

        choice = input("\nPilih menu: ").strip()

        if choice == "1":
            create_post(username)

        elif choice == "2":
            username = show_profile(username)  # ⬅️ PENTING: update username

        elif choice == "3":
            search_post()

        elif choice == "0":
            print("\n👋 Logout berhasil")
            break

        else:
            print("\n❌ Menu tidak valid")
