import tkinter as tk


# Function to perform calculations (you need to fill this with actual logic)
def calculate():
    try:
        # Retrieving values for Vehicle A
        vehicle_a_brand = vehicle_a_brand_entry.get()
        loan_a_amount = float(loan_a_brand_entry.get())
        term_length_a = int(term_length_a_entry.get())
        interest_rate_a = float(rate_a_entry.get())
        city_efficiency_a = float(city_a_entry.get())
        hwy_efficiency_a = float(hwy_a_entry.get())
        weekly_city_miles = float(weekly_city_entry.get())  # Assuming you add this for Vehicle A

        # Retrieving values for Vehicle B
        vehicle_b_brand = vehicle_b_brand_entry.get()
        loan_b_amount = float(loan_b_brand_entry.get())
        term_length_b = int(term_length_b_brand_entry.get())
        interest_rate_b = float(rate_b_brand_entry.get())
        city_efficiency_b = float(city_b_brand_entry.get())
        hwy_efficiency_b = float(hwy_b_brand_entry.get())
        weekly_hwy_miles = float(weekly_hwy_entry.get())  # Assuming you add this for Vehicle B

        # Perform calculations here ...
        final_cost_label.config(text="Super")

    except ValueError:
        # Handle invalid input
        final_cost_label.config(text="Invalid input, please enter numeric values.")

    # # Dummy values for illustration
    # monthly_maintenance_cost = 250
    # monthly_interest_charges = 150
    # monthly_loan_charges = 350
    # final_monthly_cost = 750

    # Update the labels with the calculation results
    # maintenance_cost_label.config(text=f"Car A ${monthly_maintenance_cost}")
    # interest_charges_label.config(text=f"Car A ${monthly_interest_charges}")
    # loan_charges_label.config(text=f"Car A ${monthly_loan_charges}")
    # final_cost_label.config(text=f"Car A ${final_monthly_cost}")
    # Add more updates as needed


# Main application window
root = tk.Tk()
root.title("Car Cost Calculator")

# Left frame for user inputs
left_frame = tk.Frame(root)
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Left frame for user inputs
middle_frame = tk.Frame(root)
middle_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Right frame for calculation outputs
right_frame = tk.Frame(root)
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Add input fields to the left frame
tk.Label(left_frame, text="Vehicle A Brand").pack()
vehicle_a_brand_entry = tk.Entry(left_frame)
vehicle_a_brand_entry.pack()

tk.Label(left_frame, text="Loan A Amount").pack()
loan_a_brand_entry = tk.Entry(left_frame)
loan_a_brand_entry.pack()

tk.Label(left_frame, text="Term Length A (years)").pack()
term_length_a_entry = tk.Entry(left_frame)
term_length_a_entry.pack()

tk.Label(left_frame, text="Interest rate A").pack()
rate_a_entry = tk.Entry(left_frame)
rate_a_entry.pack()


tk.Label(left_frame, text="City Efficiency A").pack()
city_a_entry = tk.Entry(left_frame)
city_a_entry.pack()

tk.Label(left_frame, text="Hwy Efficiency  A").pack()
hwy_a_entry = tk.Entry(left_frame)
hwy_a_entry.pack()

tk.Label(left_frame, text="Weekly City Miles").pack()
weekly_city_entry = tk.Entry(left_frame)
weekly_city_entry.pack()


# Add input fields to the middle frame
tk.Label(middle_frame, text="Vehicle B Brand").pack()
vehicle_b_brand_entry = tk.Entry(middle_frame)
vehicle_b_brand_entry.pack()

tk.Label(middle_frame, text="Loan B Amount").pack()
loan_b_brand_entry = tk.Entry(middle_frame)
loan_b_brand_entry.pack()

tk.Label(middle_frame, text="Term Length B (years)").pack()
term_length_b_brand_entry = tk.Entry(middle_frame)
term_length_b_brand_entry.pack()

tk.Label(middle_frame, text="Interest rate B").pack()
rate_b_brand_entry = tk.Entry(middle_frame)
rate_b_brand_entry.pack()


tk.Label(middle_frame, text="City Efficiency B").pack()
city_b_brand_entry = tk.Entry(middle_frame)
city_b_brand_entry.pack()

tk.Label(middle_frame, text="Hwy Efficiency  B").pack()
hwy_b_brand_entry = tk.Entry(middle_frame)
hwy_b_brand_entry.pack()

tk.Label(middle_frame, text="Weekly Hwy Miles").pack()
weekly_hwy_entry = tk.Entry(middle_frame)
weekly_hwy_entry.pack()


# Add a button to perform calculation
calculate_button = tk.Button(left_frame, text="Calculate", command=calculate)
calculate_button.pack()

# Add labels to the right frame for displaying outputs
maintenance_cost_label = tk.Label(right_frame, text="Monthly Maintenance Cost")
maintenance_cost_label.pack()

interest_charges_label = tk.Label(right_frame, text="Monthly Interest Charges")
interest_charges_label.pack()

loan_charges_label = tk.Label(right_frame, text="Monthly Loan Charges")
loan_charges_label.pack()

final_cost_label = tk.Label(right_frame, text="Final Monthly Cost")
final_cost_label.pack()

# ... Add more output labels here ...

# Start the application
root.mainloop()
