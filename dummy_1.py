import tkinter as tk
from tkinter import messagebox

# Conversion rates (as an example, update these rates as needed)
conversion_rates = {
    'USD': 83.00,  # Example rate: 1 USD = 83 INR
    'EUR': 89.00,  # Example rate: 1 EUR = 89 INR
    'GBP': 102.00  # Example rate: 1 GBP = 102 INR
}

# Function to convert the input currency to INR
def convert_currency():
    try:
        amount = float(entry_amount.get())
        currency = currency_var.get()
        rate = conversion_rates[currency]
        result = amount * rate
        label_result.config(text=f"{amount} {currency} = {result:.2f} INR")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid amount.")

# Create main window
window = tk.Tk()
window.title("Currency Converter")
window.geometry("300x200")

# Input amount label and entry
label_amount = tk.Label(window, text="Enter amount:")
label_amount.pack(pady=5)

entry_amount = tk.Entry(window)
entry_amount.pack(pady=5)

# Dropdown for currency selection
currency_var = tk.StringVar(value='USD')  # Default selection

label_currency = tk.Label(window, text="Choose currency:")
label_currency.pack(pady=5)

currency_menu = tk.OptionMenu(window, currency_var, 'USD', 'EUR', 'GBP')
currency_menu.pack(pady=5)

# Convert button
button_convert = tk.Button(window, text="Convert", command=convert_currency)
button_convert.pack(pady=10)

# Label to display the result
label_result = tk.Label(window, text="Converted amount will appear here")
label_result.pack(pady=10)

# Start the GUI
window.mainloop()