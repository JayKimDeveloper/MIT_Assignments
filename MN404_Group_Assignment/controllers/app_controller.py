from models.ticket_model import TicketModel
from views.login_window import LoginWindow
from views.main_window import MainWindow
from views.ticket_window import TicketWindow
from tkinter import messagebox
from views.calculate_view import CalculateView
from models.ticket_summary import TicketSummary

import tkinter as tk

class AppController:
    def __init__(self):
        self.model = TicketModel()  # define ticketModel
        self.root = tk.Tk()         # root define with tkinter
        self.root.withdraw()        # Hide main root
        self.show_login_window()    # showing the login window
        self.root.mainloop()        # start tkinter gui 

    # validate user function to call model
    def validate_user(self, username, password):
        return self.model.validate_user(username, password)

    # display login window function
    def show_login_window(self):
        self.login_window = LoginWindow(self)

    # display main window function
    def show_main_window(self):
        self.main_window = MainWindow(self)

    # logout function
    # No session, destroy the window view
    def logout(self):
        self.main_window.destroy()
        # self.show_login_window()

    # display ticket window
    def show_ticket_window(self):
        TicketWindow(self)
            
    # logic for ticket price 
    def calculate_total_price(self, ticket_counts, arena, accompanied):
        limits = {
            "Rod Laver Arena": 50,
            "Margaret Court Arena": 50,
            "John Cain Arena": 50,
            "AO Live": 10,
            "Ground Pass (Week 1)": 999,
            "Ground Pass (Middle Weekend)": 999,
            "Ground Pass (Week 2)": 999,
        }

        total_qty = sum(ticket_counts.values())
        if total_qty > limits.get(arena, 999):
            messagebox.showerror("Error", f"Ticket limit for {arena}. Max allowed: {limits[arena]}")
            return

        if ticket_counts["Kids"] > 0 and not accompanied:
            messagebox.showerror("Error", "Kids must be accompanied by an adult.")
            return

        prices = {
            "Ground Pass (Week 1)": {"adult": 49, "conc_kids": 25, "youth": 10},
            "Ground Pass (Middle Weekend)": {"adult": 69, "conc_kids": 30},
            "Ground Pass (Week 2)": {"adult": 139, "conc_kids": 70, "youth": 5},
            "Rod Laver Arena": {"adult": 75, "conc_kids": 37.5},
            "Margaret Court Arena": {"adult": 65, "conc_kids": 32.5},
            "John Cain Arena": {"adult": 65, "conc_kids": 32.5},
            "AO Live": {"adult": 20, "conc_kids": 10}
        }

        p = prices[arena]
        total_price = ( 
            0 * ticket_counts["Free"] +
            p.get("conc_kids", p["adult"]) * ticket_counts["Kids"] +
            p.get("youth", p.get("conc_kids", p["adult"])) * ticket_counts["Youth"] +
            p["adult"] * ticket_counts["Adult"] +
            p["conc_kids"] * ticket_counts["Concession"]
        )

        summary = TicketSummary(
            arena=arena,
            ticket_counts=ticket_counts,
            total_price=total_price,
            accompanied=accompanied
        )


        CalculateView(summary)


    # logic for ticket type
    def determine_ticket_type(self, age, card_type, accompanied):
        if age < 3:
            if not accompanied:
                messagebox.showerror("Error", "Children must be accompanied by an adult (18+) to enter with a Kids Ticket.")
                raise ValueError("Unaccompanied child")
            return "free"
        elif 3 <= age <= 11:
            if not accompanied:
                messagebox.showerror("Error", "Children must be accompanied by an adult (18+) to enter with a Kids Ticket.")
                raise ValueError("Unaccompanied child")
            return "conc_kids"
        elif 12 <= age <= 17:
            return "youth"
        elif age >= 18:
            if card_type != "None":
                return "conc_kids"
            else:
                return "adult"
        return "adult"

