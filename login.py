import tkinter_widgets as tk
from tkinter_widgets import messagebox
import sqlite3
import hashlib
import os

class InventoryManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("300x200")

        #self.create_database()

        self.username_label = tk.Label(root, text="Username:")
        self.username_label.pack()

        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        self.password_label = tk.Label(root, text="Password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()

        self.register_button = tk.Button(root, text="Register", command=self.register)
        self.register_button.pack()

        self.login_button = tk.Button(root, text="Login", command=self.login)
        self.login_button.pack()

    def center_window(self):
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()

            window_width = 400  # Set your desired window width
            window_height = 300  # Set your desired window height

            x = (screen_width - window_width) // 2
            y = (screen_height - window_height) // 2

            self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def is_secure_password(self, password):
        if not (8 <= len(password) <= 12):
            return False
        if not any(c.isupper() for c in password):
            return False
        if not any(c.isdigit() for c in password):
            return False
        return True

    def is_user_registered(self, username):
        self.c.execute("SELECT * FROM users WHERE username=?", (username,))
        user = self.c.fetchone()
        return user is not None

    #self.center_window()
    def create_database(self):
        self.conn = sqlite3.connect("database files/login_details.db")
        self.c = self.conn.cursor()

        self.c.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                password_hash TEXT NOT NULL,
                salt TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def insert_user(self, username, password):
        if not self.is_secure_password(password):
            messagebox.showerror("Registration Error", "Password must be 8-12 characters, include capital letters and numbers.")
            return

        if self.is_user_registered(username):
            messagebox.showerror("Registration Error", f"Username '{username}' is already registered.")
            return

        salt = self.generate_salt()
        if not salt:
            return

        else:
            password_hash = self.hash_password(password, salt)
            self.c.execute("INSERT INTO users (username, password_hash, salt) VALUES (?, ?, ?)", (username, password_hash, salt))
            self.conn.commit()

            #messagebox.showinfo("Registration", "User registered successfully!")


    def generate_salt(self):
        return hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')

    def hash_password(self, password, salt):
        return hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

    def verify_password(self, stored_password, stored_salt, entered_password):
        return stored_password == self.hash_password(entered_password, stored_salt)

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username:
            messagebox.showerror("Registration Error", "Username is required.")
            return
        if not password:
            messagebox.showerror("Registration Error", "Password is required.")
            return
        if username == password:
            messagebox.showerror("Registration Error", "Username and password cannot be the same.")
            return
        else:

            self.insert_user(username, password)
            messagebox.showinfo("Registration", "User registered successfully!")

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        self.c.execute("SELECT * FROM users WHERE username=?", (username,))
        user = self.c.fetchone()

        if user and self.verify_password(user[2], user[3], password):
            self.open_inventory_system()
        else:
            messagebox.showerror("Login Error", "Invalid username or password.")

    def open_inventory_system(self):
        # Placeholder for opening the inventory system after successful login
        messagebox.showinfo("Success", "Login successful! Opening inventory system.")

def main():
    root = tk.Tk()
    app = InventoryManagementApp(root)
    app.center_window()
    root.mainloop()

if __name__ == "__main__":
    main()
