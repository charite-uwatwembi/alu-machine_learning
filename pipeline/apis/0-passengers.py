#!/usr/bin/env python3
"""
Fetches a list of ships from the Swapi API that can hold at least a given number of passengers.
"""
import requests

def availableShips(passengerCount):
    
    url = 'https://swapi.dev/api/starships/'
    ships = []
    
    while url:  # Keep fetching as long as there's a 'next' page
        response = requests.get(url)
        data = response.json()
        
        for ship in data['results']:
            passengers = ship['passengers'].replace(',', '')  # Remove commas in large numbers
            if passengers.isdigit() and int(passengers) >= passengerCount:
                ships.append(ship['name'])
        
        # Go to the next page
        url = data['next']
    
    return ships


if __name__ == "__main__":
    """
    Test the availableShips function with different passenger counts.
    """
    ships = availableShips(4)
    for ship in ships:
        print(ship)
