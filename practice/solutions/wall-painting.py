"""Calculate how much it will cost to paint a wall."""

SQUARE_FEET_PER_GALLON = 400

print('How wide is the wall in feet?')
width_feet = float(input())
print('How tall is the wall in feet?')
height_feet = float(input())
print('How much does a gallon of paint cost in dollars?')
dollars_per_gallon = float(input())

wall_square_feet = width_feet * height_feet
wall_gallons = wall_square_feet / SQUARE_FEET_PER_GALLON
wall_dollars = dollars_per_gallon * wall_gallons

formatted_wall_dollars = str(round(wall_dollars, 2))
print('It will cost ' + formatted_wall_dollars + ' to paint the wall.')
