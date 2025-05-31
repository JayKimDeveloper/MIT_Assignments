import tkinter as tk
from tkinter import messagebox

class TicketWindow(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("AO Ticketing System")   # window title
        self.geometry("400x700")    # window size
        self.configure(bg="white")  # basic window background color
        self._init_ui()

    def _init_ui(self):
        tk.Label(self, text="AO Ticketing", font=("Arial", 20, "bold"), fg="gray", bg="white").pack(pady=20)

        self._create_label("Number of Tickets by Age Group")

        self.age_groups = {}

        # for loop for age group create label
        for label in ["Free (0-2)", "Kids (3-11)", "Youth (12-17)", "Adult (18+)", "Concession (18+ with Card)"]:
            self._create_label(label)
            self.age_groups[label] = self._create_entry()

        # check the Accompanied for kids
        self.guardian_var = tk.BooleanVar()
        tk.Checkbutton(self, text="Accompanied by an Adult (for Kids)", variable=self.guardian_var, fg="gray", bg="white").pack(pady=10)

        # Choose the arena
        self._create_label("Arena")
        self.arena_var = tk.StringVar()
        self.arena_var.set("Rod Laver Arena")
        arena_options = ["Rod Laver Arena", "Margaret Court Arena", "John Cain Arena", "AO Live", 
                        "Ground Pass (Week 1)", "Ground Pass (Middle Weekend)", "Ground Pass (Week 2)"]
        tk.OptionMenu(self, self.arena_var, *arena_options).pack(pady=5)

        # button for calculate
        tk.Button(self, text="Calculate Price", command=self.calculate_price, bg="white").pack(pady=30)



    # label function for redudancy code 
    def _create_label(self, text):
        tk.Label(self, text=text, font=("Arial", 12), fg="gray", bg="white").pack(pady=5)

    # input entry function for redudancy code
    def _create_entry(self):
        def validate_numeric_input(new_value):
            if new_value == "" or new_value.isdigit():
                return True
            else:
                messagebox.showerror("Invalid Input", "Please enter a numeric value.")
                return False

        vcmd = (self.register(validate_numeric_input), '%P')
        
        entry = tk.Entry(
            self,
            width=30,
            fg="gray",
            bg="white",
            bd=1,
            highlightthickness=1,
            validate="key",
            validatecommand=vcmd
        )
        entry.pack(pady=5)
        return entry

    def calculate_price(self):
        try:

            ticket_counts = {} # set var the ticket counts dictionary
            age_group_keys = {
                "Free": "Free (0-2)",
                "Kids": "Kids (3-11)",
                "Youth": "Youth (12-17)",
                "Adult": "Adult (18+)",
                "Concession": "Concession (18+ with Card)"
            } # define the age group keys

            # for loop, check the input value. If is not a integer, make 0
            for key, label in age_group_keys.items():
                value = self.age_groups[label].get()
                ticket_counts[key] = int(value) if value.isdigit() else 0

            print(f"ticket_counts: {ticket_counts}")

            # Showing the messagebox condtion for Concession 
            if ticket_counts["Concession"] > 0:
                messagebox.showinfo("Check", """
            You should bring one of the following:
            a) Student Cards: Full-time Secondary or Tertiary students.
            b) Pensioner Concession Card: AGE, CAR, AGE BLIND, PPS, DSP, SAL, WDA, NSA, PPP/PPS.
            c) Veteran Affairs and TPI.
            d) Health Care Cards: SA, SL, FFR, NS, YA, PPS, CD, PA, MO, FA, CDA.
            e) Personal Treatment Entitlement Card (must be current).
            """)

            # get the accompanied data and areana
            accompanied = self.guardian_var.get()
            arena = self.arena_var.get()

            # call the calculate 
            self.controller.calculate_total_price(ticket_counts, arena, accompanied)


        # If got any valid error, display the messagebox
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for all ticket counts.")

            
