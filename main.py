from components.auth import login
from components.register import register
from components.dashboard import dashboard

def header(title):
    print("\n" + "=" * 30)
    print(title.center(30))
    print("=" * 30)

def main():
    while True:
        header("PROGRAM SHUTTR CLI")
        print("1. Login")
        print("2. Register")
        print("3. Keluar")

        choice = input("\nPilih menu: ").strip()

        if choice == "1":
            username = login()
            if username:
                dashboard(username)

        elif choice == "2":
            register()

        elif choice == "3":
            print("\n- Keluar dari program")
            break

        else:
            print("\n- Pilihan tidak valid")

if __name__ == "__main__":
    main()
