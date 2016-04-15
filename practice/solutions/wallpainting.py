print('How wide is the wall in feet?')
width_feet = float(input())
print('How tall is the wall in feet?')
height_feet = float(input())
print('How much does a gallon of paint cost in dollars?')
dollars_per_gallon = float(input())
print('How many coats are you going to use?')
coats = int(input())

square_feet_per_gallon = 400
wall_square_feet = width_feet * height_feet
wall_gallons = wall_square_feet / square_feet_per_gallon * coats
wall_dollars = dollars_per_gallon * wall_gallons

print('It will cost ' + str(wall_dollars) + ' to paint the wall with ' + coats + ' coats.')
