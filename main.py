from components.auth import login
from components.register import register
from components.rbac import check_access

def header(title):
    print("\n" + "=" * 30)
    print(f"{title.center(30)}")
    print("=" * 30)

def feature_menu(username):
    header("MENU FITUR")
    print("1. Read Data")
    print("2. Write Data")
    print("3. Delete Data")
    print("0. Logout")

    choice = input("Pilih menu: ")

    actions = {
        "1": "read_data",
        "2": "write_data",
        "3": "delete_data"
    }

    if choice == "0":
        return

    action = actions.get(choice)
    if action:
        check_access(username, action)
    else:
        print("❌ Menu tidak valid")

def main():
    while True:
        header("PROGRAM SHUTTR CLI")
        print("1. Login")
        print("2. Register")
        print("3. Keluar")

        choice = input("Pilih menu: ")

        if choice == "1":
            username = login()
            if username:
                feature_menu(username)

        elif choice == "2":
            register()

        elif choice == "3":
            print("\n👋 Keluar dari program")
            break

        else:
            print("\n❌ Pilihan tidak valid")

if __name__ == "__main__":
    main()
