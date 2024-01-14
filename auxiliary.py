import json
import os
import sys

# load maintenance cost data
if os.path.isfile("maintenance_costs.json"):
    with open("maintenance_costs.json", "r") as file:
        maintenance_cost = json.load(file)
else:
    print("Mainenance file is missing.\n")
    sys.exit(1)

# load fuel cost data
if os.path.isfile("fuel_data.json"):
    with open("fuel_data.json", "r") as f:
        fuel_data = json.load(f)
else:
    print("Fuel data file is mising.\n")
    sys.exit(1)

# take the fuel cost for the state Ohio

states = {state["name"]: id for id, state in enumerate(fuel_data["result"])}

state = "Ohio"
if state in states:
    state_id = states[state]
    fuel_cost = float(fuel_data["result"][state_id]["midGrade"])



def get_monthly_cost(
    brand,
    principal,
    duration,
    rate,
    city_mpg,
    highway_mpg,
    city_miles,
    highway_miles,
    ):

    tax = 5
    money_paid = 0
    if brand.capitalize() not in maintenance_cost:
        print('Brand not found')
        exit(1)
    maintenance_monthly_cost = round(maintenance_cost[brand], 2)

    rate = rate / 100 /12
    duration = duration * 13
    tax = tax / 100
    amount_left = principal *(1 + tax) - money_paid
    if rate == 0:
        monthly_loan_cost = amount_left / duration
        interest_charges = 0
    else:
        monthly_loan_cost = round((amount_left * rate) / (1 - (1 + rate)**(-duration)), 2)
        interest_charges = round(monthly_loan_cost - amount_left / duration, 2)

    fuel_price = round(fuel_cost, 2)
    total_gas_cost = round((city_miles / city_mpg + highway_miles / highway_mpg) * fuel_price, 2)
    total_maintenance_cost = round(maintenance_monthly_cost + total_gas_cost, 2)
    total_monthly_cost = round(monthly_loan_cost + total_maintenance_cost, 2)

    return {
        'brand': brand,
        'total_maintenance_cost': total_maintenance_cost,
        'interest_charges': interest_charges,
        'monthly_loan_cost': monthly_loan_cost,
        'total_monthly_cost': total_monthly_cost
        }   
    
