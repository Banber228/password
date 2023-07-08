import tkinter as tk
import random
import string
import tkinter.messagebox as messagebox
import pyperclip


class PasswordGenerator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Password Generator")
        self.window.geometry("400x300")

        self.length_label = tk.Label(self.window, text="Password Length:")
        self.length_label.pack()

        self.length_scale = tk.Scale(self.window, from_=6, to=20, orient=tk.HORIZONTAL)
        self.length_scale.pack()

        self.count_label = tk.Label(self.window, text="Number of Passwords:")
        self.count_label.pack()

        self.count_entry = tk.Entry(self.window)
        self.count_entry.pack()

        self.generate_button = tk.Button(self.window, text="Generate", command=self.generate_passwords)
        self.generate_button.pack()

        self.password_output = tk.Text(self.window, height=10, width=30)
        self.password_output.pack()

        self.copy_button = tk.Button(self.window, text="Copy", command=self.copy_passwords)
        self.copy_button.pack()

        self.clear_button = tk.Button(self.window, text="Clear", command=self.clear_passwords)
        self.clear_button.pack()

        self.window.mainloop()

    def generate_passwords(self):
        length = int(self.length_scale.get())
        count = int(self.count_entry.get())

        characters = string.ascii_letters + string.digits + string.punctuation

        passwords = []
        for _ in range(count):
            password = "".join(random.choice(characters) for _ in range(length))
            passwords.append(password)

        self.password_output.delete("1.0", tk.END)
        for password in passwords:
            self.password_output.insert(tk.END, password + "\n")

    def copy_passwords(self):
        passwords = self.password_output.get("1.0", tk.END).strip()
        pyperclip.copy(passwords)
        messagebox.showinfo("Information", "Passwords copied to clipboard.")

    def clear_passwords(self):
        self.password_output.delete("1.0", tk.END)


PasswordGenerator()
