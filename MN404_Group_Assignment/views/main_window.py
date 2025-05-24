import tkinter as tk


class MainWindow(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("AOTMS - Main")  # window title
        self.geometry("800x600")    # window size
        self.configure(bg="white")  # basic window background color
        self._init_ui()             # initialized UI

    def _init_ui(self):
        # logo
        logo_label = tk.Label(
            self,
            text="AOTMS",
            font=("Arial", 40, "bold"),
            fg="green",
            bg="white"
        )
        logo_label.pack(pady=30)

        # cards frame
        card_frame = tk.Frame(self, bg="white")
        card_frame.pack(pady=20)

        # Card 1 - Ticketing
        self.create_card(
            card_frame,
            "Go to Ticketing",
            "Manage your tickets for upcoming events",
            self.controller.show_ticket_window
        ).pack(pady=20)

        # Card 2: Logout
        self.create_card(
            card_frame,
            "Logout",
            "Log out from your account",
            self.controller.logout
        ).pack(pady=20)

        # footer, label showing the AOTMS
        footer = tk.Label(
            self,
            text="AOTMS",
            font=("Arial", 9),
            fg="gray",
            bg="white"
        )
        footer.pack(side="bottom", pady=30)


    # card function for remove the duplication code
    def create_card(self, parent, title, description, command):

        card = tk.Frame(parent, bg="white", bd=1, relief="solid")
        card.configure(highlightbackground="white", highlightthickness=1)

        # title label
        tk.Label(
            card,
            text=title,
            font=("Arial", 16, "bold"),
            fg="gray",
            bg="white"
        ).pack(pady=(20, 10), padx=20)

        # description
        tk.Label(
            card,
            text=description,
            font=("Arial", 12),
            fg="gray",
            bg="white",
            wraplength=300
        ).pack(pady=(0, 20), padx=20)

        # button
        tk.Button(
            card,
            text="choose",
            command=command,
            font=("Arial", 12, "bold"),
            bg="white",
            fg="gray",
            activebackground="gray",
            activeforeground="white",
            bd=0,
            relief="solid",
            width=15,
            height=1,
            cursor="hand2"
        ).pack(pady=(0, 20))

        return card

