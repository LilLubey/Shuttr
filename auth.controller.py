import pandas as pd
import io

# 1. Simulate external data sources loaded into DataFrames
# Data source A: User-to-Role mapping
user_role_data = """
username,role
alice,admin
bob,user
charlie,guest
dave,user
"""
df_user_roles = pd.read_csv(io.StringIO(user_role_data))

# Data source B: Role-to-Permission mapping (Access Control List)
role_permission_data = """
role,action
admin,read_data
admin,write_data
admin,delete_data
user,read_data
user,write_data
guest,read_data
"""
df_role_permissions = pd.read_csv(io.StringIO(role_permission_data))

def check_access_from_df(username, requested_action):
    """
    Checks user permissions by querying the external DataFrames.
    """
    # Step A: Find the user's role
    user_role_row = df_user_roles.loc[df_user_roles['username'] == username]
    
    if user_role_row.empty:
        print(f"User '{username}' not found. Access denied.")
        return False
    
    user_role = user_role_row.iloc[0]['role']
    
    # Step B: Check if the role has the requested permission
    # We filter the permissions DataFrame where the role matches AND the action matches
    permission_granted = df_role_permissions.loc[
        (df_role_permissions['role'] == user_role) & 
        (df_role_permissions['action'] == requested_action)
    ]
    
    if not permission_granted.empty:
        print(f"✅ ALLOWED: '{username}' ({user_role}) can '{requested_action}'")
        return True
    else:
        print(f"❌ DENIED: '{username}' ({user_role}) cannot '{requested_action}'")
        return False

# 2. Test the access control system
print("--- RBAC Access Checks ---")
check_access_from_df('alice', 'delete_data')
check_access_from_df('bob', 'delete_data')
check_access_from_df('charlie', 'write_data')
check_access_from_df('dave', 'read_data')
check_access_from_df('eve', 'read_data') # User not in DF
