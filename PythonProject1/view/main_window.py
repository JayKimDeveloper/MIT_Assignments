from PySide6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QSpinBox, QComboBox,
    QPushButton, QVBoxLayout, QFormLayout, QMessageBox
)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self._init_ui()

    def _init_ui(self):
        self.setWindowTitle("AOTMS – Ticket Purchase")
        self.setFixedSize(600, 400)
        self.setStyleSheet("""
            QWidget {
                background-color: #0f0f1a;
                color: white;
                font-family: 'Segoe UI', sans-serif;
                font-size: 16px;
            }
            QLineEdit, QComboBox, QSpinBox {
                background-color: #1a1a2e;
                border: 1px solid #333;
                border-radius: 6px;
                padding: 6px;
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
        layout.setAlignment(Qt.AlignTop)

        title = QLabel("Purchase Your Ticket")
        title.setFont(QFont("Segoe UI", 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        form_layout = QFormLayout()
        form_layout.setFormAlignment(Qt.AlignCenter)

        self.ticket_box = QComboBox()
        self.ticket_box.addItems(self.controller.get_ticket_options())
        form_layout.addRow("Ticket Type:", self.ticket_box)

        self.age_edit = QLineEdit()
        form_layout.addRow("Age:", self.age_edit)

        self.qty_spin = QSpinBox()
        self.qty_spin.setRange(1, 50)
        form_layout.addRow("Quantity:", self.qty_spin)

        layout.addSpacing(20)
        layout.addLayout(form_layout)

        calc_btn = QPushButton("CALCULATE")
        calc_btn.clicked.connect(self._calculate)
        layout.addSpacing(30)
        layout.addWidget(calc_btn, alignment=Qt.AlignCenter)

    def _calculate(self):
        try:
            age = int(self.age_edit.text())
            qty = self.qty_spin.value()
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Enter a valid age.")
            return

        summary = self.controller.calculate_price(
            self.ticket_box.currentText(), age, qty)
        QMessageBox.information(self, "Ticket Summary", summary)
