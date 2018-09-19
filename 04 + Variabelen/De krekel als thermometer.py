# input aantal tjirps per minuut
tjirps_per_minuut = int(input("Wat is het aantal tjirps per minuut? "))

# berekenen
temperatuur_fahrenheit = 50 + ((tjirps_per_minuut - 40) / 4)
temperatuur_celsius = 10 + ((tjirps_per_minuut - 40) / 7)

# print
print("temperatuur (Fahrenheit):", temperatuur_fahrenheit)
print("temperatuur (Celsius):", temperatuur_celsius)