from PySide6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QMessageBox, QFrame
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QPalette, QColor

class LoginWindow(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self._init_ui()

    def _init_ui(self):
        self.setWindowTitle("AOTMS - Login")
        self.setFixedSize(600, 400)
        self.setStyleSheet("""
            QWidget {
                background-color: #0f0f1a;
                color: white;
                font-family: 'Segoe UI', sans-serif;
                font-size: 16px;
            }
            QLineEdit {
                background-color: #1a1a2e;
                border: 1px solid #333;
                border-radius: 6px;
                padding: 8px;
                color: white;
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

        title = QLabel("Australian Open Ticket System")
        title.setFont(QFont("Segoe UI", 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        form_frame = QFrame()
        form_layout = QVBoxLayout(form_frame)

        user_label = QLabel("User ID")
        self.user_edit = QLineEdit()

        pass_label = QLabel("Password")
        self.pass_edit = QLineEdit()
        self.pass_edit.setEchoMode(QLineEdit.Password)

        login_btn = QPushButton("LOGIN")
        login_btn.clicked.connect(self._attempt_login)

        form_layout.addWidget(user_label)
        form_layout.addWidget(self.user_edit)
        form_layout.addWidget(pass_label)
        form_layout.addWidget(self.pass_edit)
        form_layout.addSpacing(20)
        form_layout.addWidget(login_btn)

        layout.addSpacing(30)
        layout.addWidget(form_frame)

    def _attempt_login(self):
        uid = self.user_edit.text().strip()
        pw = self.pass_edit.text().strip()
        if self.controller.validate_login(uid, pw):
            self.controller.show_user_window(self)
        else:
            QMessageBox.critical(self, "Login Failed",
                                 "Credentials don't match AOTMS.\nPlease try again!")
