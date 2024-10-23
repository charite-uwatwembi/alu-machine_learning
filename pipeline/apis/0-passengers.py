#!/usr/bin/env python3

"""
This module contains a function that
uses Swapi API to get the list of ships that
can hold given number of passengers"""


def availableShips(passengerCount):
    """return empty list if no ships carry that no.
    of passengers else return list of ships"""
    import requests
    url = "https://swapi-api.alx-tools.com/api/starships/"
    ships = []

    while url:
        response = requests.get(url)
        data = response.json()
        for result in data['results']:
            if result['passengers'] != "n/a":
                passengers_no = int(result['passengers'].replace(',', ''))
                if passengers_no >= passengerCount:
                    ships.append(result['name'])
        url = data['next']

    return ships
