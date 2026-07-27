import sqlite3
import bcrypt

DATABASE = "database.db"


def login(username, password):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT password FROM users WHERE username=?",
        (username,)
    )

    user = cursor.fetchone()
    conn.close()

    if user:
        stored_password = user[0]

        if bcrypt.checkpw(
                password.encode(),
                stored_password.encode()):
            print("Login Successful")
        else:
            print("Invalid Password")

    else:
        print("User Not Found")


if __name__ == "__main__":
    username = input("Username: ")
    password = input("Password: ")

    login(username, password)