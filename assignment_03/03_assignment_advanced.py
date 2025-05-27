# Stockdale Assignment 3 - Using a GUI to enhance Exercise.
import tkinter as tk
from tkinter import messagebox

# Constants.
MIN_BANK_BALANCE = 3000
MAX_VIOLENT_FELONIES = 0
MAX_NON_VIOLENT_FELONIES = 2
MAX_VISA_DENIALS = 2
EMPLOYMENT_REQUIRED = "Yes"

# Function to evaluate user input.
def check_eligibility():
    try:
        bank_balance = float(entry_balance.get())
        violent_felonies = int(entry_violent.get())
        non_violent_felonies = int(entry_non_violent.get())
        visa_denials = int(entry_denials.get())
        employed = employment_var.get()

        eligible = True
        feedback = ""

        if bank_balance < MIN_BANK_BALANCE:
            eligible = False
            feedback += (
                f"- Your bank balance of ${bank_balance} is below the "
                f"required ${MIN_BANK_BALANCE}.\n"
            )
        if violent_felonies > MAX_VIOLENT_FELONIES:
            eligible = False
            feedback += (
                f"- You have {violent_felonies} violent felony(ies); "
                f"max allowed is {MAX_VIOLENT_FELONIES}.\n"
            )
        if non_violent_felonies > MAX_NON_VIOLENT_FELONIES:
            eligible = False
            feedback += (
                f"- You have {non_violent_felonies} non-violent felony(ies); "
                f"max allowed is {MAX_NON_VIOLENT_FELONIES}.\n"
            )
        if visa_denials > MAX_VISA_DENIALS:
            eligible = False
            feedback += (
                f"- You have {visa_denials} visa denial(s); "
                f"max allowed is {MAX_VISA_DENIALS}.\n"
            )
        if employed != EMPLOYMENT_REQUIRED:
            eligible = False
            feedback += (
                f"- Employment required: {EMPLOYMENT_REQUIRED}; "
                f"you selected '{employed}'.\n"
            )

        if eligible:
            messagebox.showinfo(
                "Result",
                "✅ Congratulations! You meet all the requirements for a "
                "tourist visa."
            )
        else:
            full_feedback = (
                "❌ You do not meet the requirements for a tourist visa.\n\n"
                "Eligibility Criteria:\n"
                f"- Bank Balance ≥ ${MIN_BANK_BALANCE}\n"
                f"- Violent Felonies ≤ {MAX_VIOLENT_FELONIES}\n"
                f"- Non-Violent Felonies ≤ {MAX_NON_VIOLENT_FELONIES}\n"
                f"- Visa Denials ≤ {MAX_VISA_DENIALS}\n"
                f"- Employment Status: {EMPLOYMENT_REQUIRED}\n\n"
                "Issues:\n" + feedback
            )
            messagebox.showwarning("Result", full_feedback)

    except ValueError:
        messagebox.showerror(
            "Input Error",
            "Please enter valid numeric values."
        )

# GUI Setup.
root = tk.Tk()
root.title("Travel Visa Eligibility Checker")

# Labels and entries.
tk.Label(root, text="Bank Balance (USD):").grid(row=0, column=0, sticky="e")
entry_balance = tk.Entry(root)
entry_balance.grid(row=0, column=1)

tk.Label(root, text="Violent Felonies:").grid(row=1, column=0, sticky="e")
entry_violent = tk.Entry(root)
entry_violent.grid(row=1, column=1)

tk.Label(root, text="Non-Violent Felonies:").grid(row=2, column=0, sticky="e")
entry_non_violent = tk.Entry(root)
entry_non_violent.grid(row=2, column=1)

tk.Label(root, text="Visa Denials:").grid(row=3, column=0, sticky="e")
entry_denials = tk.Entry(root)
entry_denials.grid(row=3, column=1)

tk.Label(root, text="Currently Employed?").grid(row=4, column=0, sticky="e")
employment_var = tk.StringVar(value="Yes")
tk.OptionMenu(root, employment_var, "Yes", "No").grid(row=4, column=1)

# Submit button.
tk.Button(
    root,
    text="Check Eligibility",
    command=check_eligibility
).grid(row=5, column=0, columnspan=2, pady=10)

# Run the GUI loop.
root.mainloop()