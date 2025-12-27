from components.post import create_post
from components.profile import show_profile
from components.search import search_post
from components.logout import logout
from components.auth import get_current_user

def header(title):
    print("\n" + "=" * 30)
    print(title.center(30))
    print("=" * 30)

def dashboard():
    user = get_current_user()
    if not user:
        print("❌ Silakan login terlebih dahulu")
        return

    while True:
        header("MENU DASHBOARD")
        print(f"Login sebagai: {user}\n")

        print("1. Post forum")
        print("2. Profil")
        print("3. Cari postingan")
        print("0. Logout")

        choice = input("\nPilih menu: ").strip()

        if choice == "1":
            create_post(user)

        elif choice == "2":
            show_profile(user)

        elif choice == "3":
            search_post()

        elif choice == "0":
            logout()
            break

        else:
            print("\n❌ Menu tidak valid")
