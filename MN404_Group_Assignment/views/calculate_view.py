import tkinter as tk
from tkinter import messagebox
from models.ticket_summary import TicketSummary

class CalculateView(tk.Toplevel):
    def __init__(self, summary: TicketSummary):
        super().__init__()
        self.title("Ticket Summary") # window title
        self.geometry("350x350")     # window size
        self.configure(bg="white")   # window basic background color - white

        tk.Label(self, text="Ticket Summary", font=("Arial", 16, "bold"), fg="black", bg="white").pack(pady=10)
        tk.Label(self, text=f"Arena: {summary.arena}", font=("Arial", 12), fg="black", bg="white").pack(pady=5)
        
        # Check the accompanied data with if summary.accompanied
        tk.Label(self, text=f"Accompanied: {'Yes' if summary.accompanied else 'No'}", font=("Arial", 12), fg="black", bg="white").pack(pady=5)

        tk.Label(self, text="Tickets:", font=("Arial", 12, "underline"), fg= "black", bg="white").pack(pady=5)
        for category, count in summary.ticket_counts.items():
            if count > 0:
                tk.Label(self, text=f"{category}: {count}", font=("Arial", 11), fg="black", bg="white").pack()

        tk.Label(self, text=f"Total Price: ${summary.total_price:.2f}", font=("Arial", 13, "bold"),fg="black", bg="white").pack(pady=10)

        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        # OK burtton
        tk.Button(button_frame, text="payment", width=10, command=lambda: self.confirm_purchase(summary)
        , bg="green", fg="black").pack(side="left", padx=10)

        # Cancel button
        tk.Button(button_frame, text="Cancel", width=10, command=self.destroy
        , bg="red", fg="black").pack(side="right", padx=10)

    # Showing the purchase infomation
    def confirm_purchase(self, summary: TicketSummary):
        summary_str = (
            f"Arena: {summary.arena}\n"
            f"Qty: {summary.ticket_counts}\n"
            f"Total: {summary.total_price}"
        )
        
        messagebox.showinfo("Purchase", summary_str)
        self.destroy()
