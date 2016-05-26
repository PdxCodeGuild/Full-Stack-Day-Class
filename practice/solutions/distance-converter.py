"""
"""

meters_per_kilometer = 1000
meters_per_foot = 1 / 3.2808398950131
feet_per_mile = 5280

input_amount = float(input('Amount: '))
input_units = input('Starting units: ')
output_units = input('Requested units: ')

if input_units == 'm':
    meter_amount = input_amount
elif input_units == 'km':
    meter_amount = input_amount * meters_per_kilometer
elif input_units == 'ft':
    meter_amount = input_amount * meters_per_foot
elif input_units == 'mi':
    meter_amount = input_amount * feet_per_mile * meters_per_foot

if output_units == 'm':
    output_amount = meter_amount
elif output_units == 'km':
    output_amount = meter_amount / meters_per_kilometer
elif output_units == 'ft':
    output_amount = meter_amount / meters_per_foot
elif output_units == 'mi':
    output_amount = meter_amount / feet_per_mile / meters_per_foot

print(input_amount + ' ' + input_units + ' is ' + output_amount + ' ' +
      output_units)
