import pandas as pd

def login():
    credentials = pd.read_csv("dataframe.csv")

    credentials.columns = credentials.columns.str.strip()

    credentials['email'] = credentials['email'].astype(str)
    credentials['username'] = credentials['username'].astype(str)
    credentials['password'] = credentials['password'].astype(str)

    credentials['email'] = credentials['email'].str.strip()
    credentials['username'] = credentials['username'].str.strip()
    credentials['password'] = credentials['password'].str.strip()

    while True:
        entered_email = input("Enter email: ").strip()
        entered_username = input("Enter username: ").strip()
        entered_password = input("Enter password: ").strip()

        match = credentials[
            (credentials['email'] == entered_email) & 
            (credentials['username'] == entered_username) & 
            (credentials['password'] == entered_password)
        ]

        if not match.empty:
            print("Login successful!")
            break
        else:
            print("Invalid, Try again.\n")

if __name__ == "__main__":
    login()