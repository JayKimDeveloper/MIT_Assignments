from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class UserWindow(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self._init_ui()

    def _init_ui(self):
        self.setWindowTitle("AOTMS – Welcome")
        self.setFixedSize(600, 400)
        self.setStyleSheet("""
            QWidget {
                background-color: #0f0f1a;
                color: white;
                font-family: 'Segoe UI';
                font-size: 16px;
            }
            QPushButton {
                background-color: #0055aa;
                border: none;
                padding: 10px;
                border-radius: 8px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #0077dd;
            }
        """)

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)

        label = QLabel("Welcome, User!")
        label.setFont(QFont("Segoe UI", 20, QFont.Bold))
        label.setAlignment(Qt.AlignCenter)

        start_btn = QPushButton("Proceed to Main Menu")
        start_btn.clicked.connect(self._go_main)

        logout_btn = QPushButton("Logout")
        logout_btn.clicked.connect(self._logout)

        layout.addWidget(label)
        layout.addSpacing(20)
        layout.addWidget(start_btn)
        layout.addWidget(logout_btn)

    def _logout(self):
        self.controller.show_login_window(self)

    def _go_main(self):
        self.controller.show_main_window(self)
