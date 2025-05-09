from PySide6.QtWidgets import QApplication
import sys
from model.ticket_data import TICKETS, USERS
from view.login_window import LoginWindow
from view.main_window  import MainWindow
from  view.user_window import UserWindow

class AppController:
    # ─── model helpers ───────────────────────────────────────────────
    def get_ticket_options(self):
        return list(TICKETS.keys())

    def calculate_price(self, ticket, age, qty):
        adult, concession = TICKETS[ticket]
        if age <= 2:
            cat, price = "Free (under 3)", 0
        elif 3 <= age <= 11:
            cat, price = "Kids", concession
        elif 12 <= age <= 17:
            cat = "Youth"; price = adult if "Youth" in ticket else concession
        else:
            cat, price = "Adult", adult
        total = price * qty
        return (
            f"Ticket Type: {ticket}\nAge Category: {cat}\n"
            f"Unit Price: ${price:.2f}\nQuantity: {qty}\nTotal: ${total:.2f}"
        )

    # ─── auth ────────────────────────────────────────────────────────
    def validate_login(self, uid, pw):
        return USERS.get(uid) == pw

    # ─── Qt window orchestration ─────────────────────────────────────
    def start(self):
        self.app = QApplication(sys.argv)
        self.login = LoginWindow(self)
        self.login.show()
        sys.exit(self.app.exec())

    def show_login_window(self, user_widget):
        self.login.show()
        user_widget.close()


    def show_main_window(self, user_widget):
        self.main_screen = MainWindow(self)
        self.main_screen.show()
        user_widget.close()

    def show_user_window(self, login_widget):
        self.user_screen = UserWindow(self)
        self.user_screen.show()
        login_widget.close()

    def _logout(self):
        self.login_window = LoginWindow(self.controller)
        self.login_window.show()
        self.close()