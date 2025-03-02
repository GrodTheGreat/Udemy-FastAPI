"""
- given my_vehicle = {'model': 'Ford', 'make': 'Explorer', 'year': 2018, 'milage': 40000}
- create a for loop to print all keys and values
- create a new variable vehicle2, which is a copy of my_vehicle
- add a new key 'number_of_tires' to the vehicle2 variable that is equal to 4
- delete the mileage key and value from vehicle2
- print just the keys from vehicle2
"""

my_vehicle = {"model": "Ford", "make": "Explorer", "year": 2018, "milage": 40_000}

for key, value in my_vehicle.items():
    print(f"Key: {key}, Value: {value}")

vehicle2 = my_vehicle.copy()
vehicle2["number_of_tires"] = 4
vehicle2.pop("milage")
print(vehicle2.keys())
