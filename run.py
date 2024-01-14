import tkinter as tk

from auxiliary import get_monthly_cost


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

        print(vehicle_a_brand, loan_a_amount, term_length_a, interest_rate_a, city_efficiency_a, hwy_efficiency_a)

        # Retrieving values for Vehicle B
        vehicle_b_brand = vehicle_b_brand_entry.get()
        loan_b_amount = float(loan_b_brand_entry.get())
        term_length_b = int(term_length_b_brand_entry.get())
        interest_rate_b = float(rate_b_brand_entry.get())
        city_efficiency_b = float(city_b_brand_entry.get())
        hwy_efficiency_b = float(hwy_b_brand_entry.get())

        weekly_city_miles = float(weekly_city_entry.get())
        weekly_hwy_miles = float(weekly_hwy_entry.get())

        print(vehicle_b_brand, loan_b_amount, term_length_b, interest_rate_b, city_efficiency_b, hwy_efficiency_b)
        monthly_cost_car_a = get_monthly_cost(
            vehicle_a_brand,
            loan_a_amount,
            term_length_a,
            interest_rate_a,
            city_efficiency_a,
            hwy_efficiency_a,
            weekly_city_miles,
            weekly_hwy_miles,
            )

        monthly_cost_car_b = get_monthly_cost(
            vehicle_b_brand,
            loan_b_amount,
            term_length_b,
            interest_rate_b,
            city_efficiency_b,
            hwy_efficiency_b,
            weekly_city_miles,
            weekly_hwy_miles,
        )

    except ValueError:
        # Handle invalid input
        error_label = tk.Label(right_frame, text="Error:",)
        error_label.pack()
        error_label.config(text="Invalid input, please enter numeric values.")
        return

    # Add labels to the right frame for displaying outputs
    maintenance_cost_label = tk.Label(right_frame, text="Monthly Maintenance Cost", state='disabled')
    maintenance_cost_label.pack()

    maintenance_cost_display = tk.Label(right_frame, text=f"Car A: ${monthly_cost_car_a['total_maintenance_cost']}\nCar B: ${monthly_cost_car_b['total_maintenance_cost']}"
    )
    maintenance_cost_display.pack()


    interest_charges_label = tk.Label(right_frame, text="Monthly Interest Charges", state='disabled')
    interest_charges_label.pack()
    
    interest_charges_display = tk.Label(right_frame, text=f"Car A: ${monthly_cost_car_a['interest_charges']}\nCar B: ${monthly_cost_car_b['interest_charges']}"
    )
    interest_charges_display.pack()
    
    loan_charges_label = tk.Label(right_frame, text="Monthly Loan Charges", state='disabled')
    loan_charges_label.pack()

    loan_charges_display = tk.Label(right_frame, text=f"Monthly Loan Charges\nCar A: ${monthly_cost_car_a['monthly_loan_cost']}\nCar B: ${monthly_cost_car_b['monthly_loan_cost']}"
    )
    loan_charges_display.pack()


    final_cost_label = tk.Label(right_frame, text="Final Monthly Cost", state='disabled')
    final_cost_label.pack()

    final_cost_display = tk.Label(right_frame, text=f"Final Monthly Cost\nCar A: ${monthly_cost_car_a['total_monthly_cost']}\nCar B: ${monthly_cost_car_b['total_monthly_cost']}"
    )
    final_cost_display.pack()

    most_convenient_car_cost = monthly_cost_car_a if monthly_cost_car_a["total_monthly_cost"] <  monthly_cost_car_b["total_monthly_cost"] else monthly_cost_car_b

    car_to_buy_label = tk.Label(right_frame, text="Car To Buy", state='disabled')
    car_to_buy_label.pack()

    car_to_buy_display = tk.Label(right_frame, text=f"{most_convenient_car_cost['brand']}", font=('Arial', 32))
    car_to_buy_display.pack()

    # Add a label to display the total cost of ownership
    total_cost_label = tk.Label(right_frame, text="Total Car Cost of Ownership", state='disabled')
    total_cost_label.pack()

    total_cost_display = tk.Label(right_frame, text=f"${most_convenient_car_cost['total_monthly_cost']}")
    total_cost_display.pack()

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

# Start the application
root.mainloop()
