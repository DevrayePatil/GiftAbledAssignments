cities = ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai"]

print("List of Cities:")
for city in cities:
    print(city)


cities.remove("Delhi")
print("\nList of Cities after removing Delhi:")
for city in cities:
    print(city)

cities.append("Kolkata")
print("\nList of Cities after adding Kolkata:")
for city in cities:
    print(city)