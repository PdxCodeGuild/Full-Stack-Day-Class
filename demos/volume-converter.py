"""Convert a volume in gallons to liters."""
# 1. Setup
liters_per_gallon = 3.785411784

# 2. Input
print('How many gallons?')
gallons = float(input())

# 3. Transform
liters = liters_per_gallon * gallons

# 4. Output
print(str(gallons) + ' gallons is ' + str(liters) + ' liters.')
