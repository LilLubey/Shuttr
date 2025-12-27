# components/logout.py

from components.auth import get_current_user, set_current_user

def logout():
    user = get_current_user()

    if not user:
        print("❌ Belum ada user yang login")
    else:
        print(f"\n👋 User {user} berhasil logout")
        set_current_user(None)
