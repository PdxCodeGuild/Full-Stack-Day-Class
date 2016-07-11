# Stubbing

**Stubbing** is writing out function definitions without filling in the body, just to feel the structure of your code.
I think of it as "coding by making believe".

Start by defining a real main function and calling pretend functions for each one of the steps you'll think you have in your problem.

```py
def main():
    """Find the distance between two cities."""
    city_one = prompt_for_city()
    city_two = prompt_for_city()
    coordinates_one = lookup_coordinates_for_city(city_one)
    coordinates_two = lookup_coordinates_for_city(city_two)
    distance_one_two = calculate_distance(coordinates_one, coordinates_two)
    print_distance(city_one, city_two, distance_one_two)
```

Then add definitions for those pretend functions you just used.
In them, write out code that comes to mind, or use more pretend functions for steps in that sub-problem.

```py
def lookup_coordinates_for_city(city_string):
    zip_code = lookup_zipcode(city_string)
    return translate_zipcode_to_coordinates(zip_code)
```

Repeat this process until all of your functions are real code!
