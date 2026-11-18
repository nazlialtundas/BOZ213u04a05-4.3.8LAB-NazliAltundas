def liters_100km_to_miles_gallon(liters):
    gallons = liters / 3.78541
    miles = 100 * 1000 / 1609.344
    return miles / gallons


def miles_gallon_to_liters_100km(miles):
    gallons = 100 * 1000 / 1609.344 / miles
    liters = gallons * 3.78541
    return liters


print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
