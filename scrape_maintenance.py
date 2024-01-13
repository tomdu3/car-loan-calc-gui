from bs4 import BeautifulSoup
import requests
import sys
import os
import json

def get_maintenance_cost():
    '''get maintenance cost data from caredge.com'''

    url = 'https://caredge.com/ranks/maintenance/'
    
    # check if the file already exists
    if os.path.isfile('maintenance_costs.json'):
        update_cost = input(
                'Would you like to update the maintenance cost data? (y/n) '
                )
        if update_cost.lower() != 'y':
            with open('maintenance_costs.json', 'r') as file:
                maintenance_cost = json.load(file)
            return maintenance_cost
    response = requests.get(url)
    if response.status_code != 200:
        print('Error retrieving data')
        print(response.status_code)
        print(response.text)
        sys.exit(1)

    print('Maintenance data retrieved successfully')
    soup = BeautifulSoup(response.text, 'html.parser')
    tables = soup.find_all('table')
    table = tables[0]
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    maintenance_cost = {}
    for row in rows:
        cols = row.find_all('td')
        cols = [el.text.strip() for el in cols]
        # convert 10 year maintenance cost to monthly cost
        maintenance_cost[cols[1]] = int(cols[2]
                                        .replace('$', '')
                                        .replace(',', ''))/10/12

    with open('maintenance_costs.json', 'w') as file:
        json.dump(maintenance_cost, file)

    return maintenance_cost

get_maintenance_cost()
