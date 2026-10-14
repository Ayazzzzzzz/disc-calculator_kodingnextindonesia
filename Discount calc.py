import tkinter as tk
from tkinter import messagebox

# ==============================================================================
# TEACHER NOTE: 
# The detailed notes below are meant as a self-study guide or recall material 
# for students. They don't need to type every single comment manually!
# ==============================================================================

# ==========================================
# DISCOUNT CALCULATOR APPLICATION
# ==========================================

# Main function to calculate the total price after applying a discount
def calculate_discount():
    # Try-except block acts as our safety net! 
    # If a student accidentally types letters or leaves fields blank, 
    # the app won't crash; it will catch the error and pop up a friendly warning.
    try:
        # Step 1: Grab the values entered by the user
        
        # Why float()? Because prices can have decimals (cents or fractional values).
        original_price = float(entry_price.get())
        discount_percent = float(entry_discount.get())
        
        # Why int()? Because item quantity must be a whole number (e.g., buying 2 books, not 2.5).
        quantity = int(entry_quantity.get())
        
        # Step 2: Quick validation to prevent weird logic (no negative prices or zero items)
        if original_price < 0 or discount_percent < 0 or quantity <= 0:
            messagebox.showerror("Error", "Price, discount, and quantity must be positive numbers!")
            return

        # Step 3: Do the math
        subtotal = original_price * quantity
        discount_amount = subtotal * (discount_percent / 100)
        final_price = subtotal - discount_amount

        # Step 4: Show the final result on the screen
        # The ':,.2f' trick formats the number nicely with thousand separators and 2 decimal places.
        label_result.config(text=f"Final Price: Rp. {final_price:,.2f}")
        
    except ValueError:
        # Catches any text typos or empty inputs and warns the user nicely
        messagebox.showerror("Invalid Input", "Please enter valid numbers only!")

# ==========================================
# MAIN WINDOW SETUP (GUI)
# ==========================================
root = tk.Tk()
root.title("Discount Calculator")
root.geometry("400x420")
root.config(bg="#f0f0f0")

# Main title label at the top of the window
label_title = tk.Label(root, text="Discount Calculator", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333333")
label_title.pack(pady=10)

# ==============================================================================
# COPY-PASTE REUSE PATTERN:
# The Frame and Input block below is a reusable pattern. You can easily copy 
# and paste it if you want to add another input field later (like a tax field)!
# ==============================================================================

# Frame for Original Price Input
# Frames help group related items together so everything stays neat and organized.
frame_price = tk.Frame(root, bg="#f0f0f0")
frame_price.pack(pady=5) # 'pack' automatically stacks elements vertically from top to bottom.
label_price = tk.Label(frame_price, text="Original Price:", font=("Arial", 11), bg="#f0f0f0")
label_price.pack()
entry_price = tk.Entry(frame_price, font=("Arial", 11), width=25)
entry_price.pack(pady=2)

# Frame for Discount Percentage Input (Copy-paste template)
frame_discount = tk.Frame(root, bg="#f0f0f0")
frame_discount.pack(pady=5)
label_discount = tk.Label(frame_discount, text="Discount (%):", font=("Arial", 11), bg="#f0f0f0")
label_discount.pack()
entry_discount = tk.Entry(frame_discount, font=("Arial", 11), width=25)
entry_discount.pack(pady=2)

# Frame for Quantity Input
frame_quantity = tk.Frame(root, bg="#f0f0f0")
frame_quantity.pack(pady=5)
label_quantity = tk.Label(frame_quantity, text="Quantity:", font=("Arial", 11), bg="#f0f0f0")
label_quantity.pack()
entry_quantity = tk.Entry(frame_quantity, font=("Arial", 11), width=25)
entry_quantity.pack(pady=2)
entry_quantity.insert(0, "1") # Sets a handy default value of 1 so students don't start with a blank box

# Calculate Button
# The 'command' parameter links this physical button to our calculate_discount function when clicked.
btn_calculate = tk.Button(root, text="Calculate", font=("Arial", 11, "bold"), bg="#4CAF50", fg="white", width=15, command=calculate_discount)
btn_calculate.pack(pady=15)

# Label to Display Final Result
label_result = tk.Label(root, text="Final Price: Rp. 0.00", font=("Arial", 12, "bold"), bg="#f0f0f0", fg="#2e7d32")
label_result.pack(pady=5)

# ==========================================
# APPLICATION RUNNER (LOOP)
# ==========================================
# This is the "heartbeat" of any GUI app. 
# It keeps the window open and continuously listens for user clicks or typing events.
root.mainloop()