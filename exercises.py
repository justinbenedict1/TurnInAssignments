# 1. Declare and assign the variables here:
shuttle_name = 'Determination'
shuttle_speed_mph = 17500
distance_to_mars_km = 225000000
distance_to_moon_km = 38400
MILES_PER_KM = 0.621
# 2. Use print() to print the 'type' each variable. Print one item per line.
print(type(shuttle_name))
print(type(shuttle_speed_mph))
print(type(distance_to_mars_km))
print(type(distance_to_moon_km))
print(type(MILES_PER_KM))
'''<class 'str'>
<class 'int'>
<class 'int'>
<class 'int'>
<class 'float'>'''
# Code your solution to exercises 3 and 4 here:
Miles_to_mars = distance_to_mars_km * MILES_PER_KM
print(Miles_to_mars)
'''139725000.0'''
hours_to_mars = Miles_to_mars / shuttle_speed_mph
print (hours_to_mars)
'''7984.285714285715'''
days_to_mars = hours_to_mars / 24
print (f"Days to mars = {(days_to_mars)}")
'''Days to mars = 332.67857142857144'''

print (f"{shuttle_name} will take {days_to_mars} days to reach Mars.")

'''Determination will take 332.67857142857144 days to reach Mars.'''
# Code your solution to exercise 5 here
miles_to_moon = distance_to_moon_km * MILES_PER_KM
hours_to_moon = miles_to_moon / shuttle_speed_mph
days_to_moon = hours_to_moon / 24

print(f"{shuttle_name} will take {days_to_moon} days to reach the Moon.")
'''Determination will take 0.05677714285714286 days to reach the Moon.'''