import bcrypt
import sqlite3

DATABASE = "database.db"


def register_user(username, password):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    hashed_password = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )

    try:
        cursor.execute(
            "INSERT INTO users(username, password) VALUES (?, ?)",
            (username, hashed_password.decode())
        )

        conn.commit()
        print("User registered successfully.")

    except sqlite3.IntegrityError:
        print("Username already exists.")

    finally:
        conn.close()


if __name__ == "__main__":
    username = input("Username: ")
    password = input("Password: ")

    register_user(username, password)