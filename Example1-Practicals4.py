import sqlite3
import os

# Insecure function to demonstrate SQL injection vulnerability
def unsafe_query(database_file, user_input):
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + user_input + "'"
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

# Function demonstrating command injection vulnerability
def delete_user_file(username):
    # Insecurely deleting a file based on user input
    os.system("rm -rf /home/app/" + username)

# Function demonstrating insecure file handling
def read_sensitive_file():
    # Hard-coded path to a sensitive file
    with open("/etc/passwd", 'r') as file:
        content = file.read()
    return content

# Hard-coded credentials, demonstrating poor security practice
def connect_to_db():
    username = "admin"
    password = "admin123"  # Never hard-code passwords!
    conn = sqlite3.connect(f'dbfile?user={username}&password={password}')
    return conn

# Demonstrate a lack of input validation leading to buffer overflow
def get_user_details(user_id):
    buffer = [""] * 10  # buffer with fixed size
    buffer[int(user_id)] = "User Details"  # potential buffer overflow if user_id is not validated
    return buffer

# Main function to simulate application logic
def main():
    username = input("Enter your username: ")
    print("User details:", unsafe_query("application.db", username))
    print("Trying to delete user files...")
    delete_user_file(username)
    print("Reading sensitive file content:")
    print(read_sensitive_file())

if __name__ == "__main__":
    main()
