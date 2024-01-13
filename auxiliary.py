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
    fuel_cost = fuel_data["result"][state_id]["midGrade"]

print(fuel_cost)


def get_monthly_cost(
    vehicle_b_brand,
    loan_b_amount,
    term_length_b,
    interest_rate_b,
    city_efficiency_b,
    hwy_efficiency_b,
    weekly_city_miles,
    weekly_hwy_miles,
):
    pass
