import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

USER_ROLE_PATH = os.path.join(BASE_DIR, "data", "user_roles.csv")
ROLE_PERMISSION_PATH = os.path.join(BASE_DIR, "data", "role_permissions.csv")

def check_access(username, action):
    df_user_roles = pd.read_csv(USER_ROLE_PATH)
    df_role_permissions = pd.read_csv(ROLE_PERMISSION_PATH)

    user_row = df_user_roles[df_user_roles["username"] == username]

    if user_row.empty:
        print(f"❌ User '{username}' tidak punya role")
        return False

    role = user_row.iloc[0]["role"]

    permission = df_role_permissions[
        (df_role_permissions["role"] == role) &
        (df_role_permissions["action"] == action)
    ]

    if not permission.empty:
        print(f"✅ ALLOWED: {username} ({role}) → {action}")
        return True
    else:
        print(f"❌ DENIED: {username} ({role}) → {action}")
        return False
