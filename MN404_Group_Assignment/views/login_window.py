import tkinter as tk
from tkinter import messagebox


class LoginWindow(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("AOTMS Login") # program title 
        self.geometry("700x600")  # program size
        self.configure(bg="white") #program basic setting color
        self._init_ui() # initialized UI

    #initial UI Content
    def _init_ui(self):
        #  logo
        tk.Label(
            self, text="AOTMS", font=("Arial", 30, "bold"), fg="green", bg="white").pack(pady=40)

        # ID input field
        self.username_entry = tk.Entry(
            self,
            width=30,
            font=("Arial", 12),
            fg="gray",
            bg="white",
            relief="solid",         # ← border line solid
            bd=1,                   # ← border width
            highlightbackground="gray",  # ← basic border color
            highlightcolor="green",      # ← focus border color
            highlightthickness=1,
            insertbackground="green"
        )
        self.username_entry.pack(pady=10, ipady=10)
        self.username_entry.focus_set()  # Cursor Auto Focus

        # Password input field
        self.password_entry = tk.Entry(
            self,
            width=30,
            font=("Arial", 12),
            fg="gray",
            bg="white",
            relief="solid",         # border line solid
            bd=1,                   # border width
            highlightbackground="gray",  # basic border color
            highlightcolor="green",      # focus border color
            highlightthickness=1,
            insertbackground="green",
            show="*"  # 입력한 텍스트를 *로 표시
        )

        self.password_entry.pack(pady=10, ipady=10)

        # Login Button
        button = tk.Button(
            self,
            text="LOGIN",
            command=self.login,
            font=("Arial", 11, "bold"),
            bg="#03C75A",  # button color
            fg="#666",  # font color
            bd=0,  # delete the border line
            width=25,
            height=2
        )
        button.pack(pady=30)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.controller.validate_user(username, password):
            self.destroy()  # Closed button, closed the root
            self.controller.show_main_window()  # MainWindow starts with new tk.TK
        else:
            messagebox.showerror("Failed", "The username or password does not match.")


