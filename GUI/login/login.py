import mysql.connector
from mysql.connector import Error
from werkzeug.security import generate_password_hash, check_password_hash

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='HiIchbincool3',
            database='Local instance MySQL80'
        )
        return connection
    except Error as e:
        print(f"Error connecting to database: {e}")
        return None

def authenticate_user(username, password):
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
            result = cursor.fetchone()
            if result and check_password_hash(result[0], password):
                return True
        except Error as e:
            print(f"Error authenticating user: {e}")
        finally:
            if connection.is_connected():
                connection.close()
    return False

def main():
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if authenticate_user(username, password):
            print("Authentication successful!")
            break
        else:
            print("Invalid username or password. Please try again.")

if __name__ == "__main__":
    main()
