import requests
import json
import dotenv
import os
import sys

# Load the environment variables

if os.path.isfile('.env'):
    dotenv.load_dotenv()
    print('Environment variables loaded')

## remove the following lines if deploying to heroku
else:
    print('Environment variables not loaded')
    sys.exit(1)

# set the API key and URL
RAPID_API_KEY = os.getenv('RAPID_API_KEY')
RAPID_URL = 'https://gas-price.p.rapidapi.com/allUsaPrice'



def get_fuel_us():
    '''Get the fuel cost data from the RAPID API'''
    fuel_headers = {
        'X-RapidAPI-Key': RAPID_API_KEY,
        'X-RapidAPI-Host': 'gas-price.p.rapidapi.com'
    }
    response = requests.get(RAPID_URL, headers=fuel_headers)
    if response.status_code == 200:
        print('US Fuel Prices data retrieved successfully')
        with open('fuel_data.json', 'w') as f:
            json.dump(response.json(), f)
    else:
        print('Error retrieving data')
        print(response.status_code)
        print(response.text)
        sys.exit(1)


def get_fuel_cost():
    '''Get the fuel cost data from the RAPID API'''
    if os.path.isfile('fuel_data.json'):
        update_cost = input('Would you like to update the fuel cost data?'
                            '(y/n) ')
        if update_cost.lower() == 'y':
            get_fuel_us()
    else:
        get_fuel_us()

    with open('fuel_data.json', 'r') as f:
        fuel_data = json.load(f)

    # check if data was not retrieved successfully
    if not fuel_data['success']:
        print('Error retrieving data')
        sys.exit(1)


get_fuel_cost()
print('Fuel cost data retrieved successfully')
