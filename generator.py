import tkinter as tk
import random
import string
import tkinter.messagebox as messagebox
import pyperclip


class PasswordGenerator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Генератор паролів")
        self.window.geometry("400x500")
        self.window.configure(bg="#f2f2f2")  # Зміна фонового кольору

        self.title_label = tk.Label(self.window, text="Генератор паролів", font=("Arial", 16, "bold"), bg="#f2f2f2")
        self.title_label.pack(pady=10)

        self.length_label = tk.Label(self.window, text="Довжина паролю:", bg="#f2f2f2")
        self.length_label.pack()

        self.length_scale = tk.Scale(self.window, from_=6, to=20, orient=tk.HORIZONTAL, bg="#f2f2f2")
        self.length_scale.set(10)  # Значення за замовчуванням
        self.length_scale.pack()

        self.count_label = tk.Label(self.window, text="Кількість паролів:", bg="#f2f2f2")
        self.count_label.pack()

        self.count_entry = tk.Entry(self.window)
        self.count_entry.pack()

        self.strength_label = tk.Label(self.window, text="Сила паролю:", bg="#f2f2f2")
        self.strength_label.pack()

        self.strength_var = tk.StringVar()
        self.strength_combobox = tk.OptionMenu(self.window, self.strength_var, "Слабка", "Середня", "Сильна")
        self.strength_combobox.pack()

        self.include_uppercase = tk.BooleanVar()
        self.uppercase_checkbox = tk.Checkbutton(self.window, text="Включити великі літери", variable=self.include_uppercase, bg="#f2f2f2")
        self.uppercase_checkbox.pack()

        self.include_digits = tk.BooleanVar()
        self.digits_checkbox = tk.Checkbutton(self.window, text="Включити цифри", variable=self.include_digits, bg="#f2f2f2")
        self.digits_checkbox.pack()

        self.include_special_chars = tk.BooleanVar()
        self.special_chars_checkbox = tk.Checkbutton(self.window, text="Включити спеціальні символи", variable=self.include_special_chars, bg="#f2f2f2")
        self.special_chars_checkbox.pack()

        self.generate_button = tk.Button(self.window, text="Згенерувати", command=self.generate_passwords, bg="#f2f2f2")
        self.generate_button.pack(pady=10)

        self.password_output = tk.Text(self.window, height=10, width=30)
        self.password_output.pack()

        self.copy_button = tk.Button(self.window, text="Скопіювати", command=self.copy_passwords, bg="#f2f2f2")
        self.copy_button.pack(pady=10)

        self.clear_button = tk.Button(self.window, text="Очистити", command=self.clear_passwords, bg="#f2f2f2")
        self.clear_button.pack()

        self.window.mainloop()

    def generate_passwords(self):
        length = int(self.length_scale.get())
        count = self.count_entry.get()
        strength = self.strength_var.get()

        if not count.isdigit():
            messagebox.showerror("Помилка", "Будь ласка, введіть дійсне значення кількості паролів.")
            return

        count = int(count)
        include_uppercase = self.include_uppercase.get()
        include_digits = self.include_digits.get()
        include_special_chars = self.include_special_chars.get()

        characters = string.ascii_lowercase
        if include_uppercase:
            characters += string.ascii_uppercase
        if include_digits:
            characters += string.digits
        if include_special_chars:
            characters += string.punctuation

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
        messagebox.showinfo("Інформація", "Пароль скопійований в буфер обміну.")

    def clear_passwords(self):
        self.password_output.delete("1.0", tk.END)


PasswordGenerator()
