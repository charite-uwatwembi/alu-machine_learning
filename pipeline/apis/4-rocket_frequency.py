#!/usr/bin/env python3
"""Pipeline Api"""
import requests

if __name__ == '__main__':
    """pipeline api"""
    url = "https://api.spacexdata.com/v4/launches"
    r = requests.get(url)

# Dictionary to count launches by rocket ID dynamically
    rocket_dict = {}

    # Count launches per rocket ID
    for launch in r.json():
        rocket_id = launch["rocket"]
        if rocket_id in rocket_dict:
            rocket_dict[rocket_id] += 1
        else:
            rocket_dict[rocket_id] = 1

    # Sorted dictionary of rocket counts
    sorted_rockets = sorted(rocket_dict.items(), key=lambda kv: kv[1], reverse=True)
    
    # Print results with rocket names
    for key, value in sorted_rockets:
        rurl = "https://api.spacexdata.com/v4/rockets/" + key
        req = requests.get(rurl)
        rocket_name = req.json().get("name", "Unknown Rocket")
        print(f"{rocket_name}: {value}")
