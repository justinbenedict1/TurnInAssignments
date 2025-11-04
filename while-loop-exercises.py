# Define three variables for the LaunchCode shuttle - one for the starting fuel level, another for the number of astronauts aboard, and the third for the altitude the shuttle reaches.
starting_fuel_level = int(input("Enter starting fuel level: "))
astros_onboard = int(input("Enter astros onboard level: "))
altitude = 0
# Exercise #1: Construct while loops to do the following:
  # a. Query the user for the starting fuel level. Validate that the user enters a positive, integer value greater than 5000 but less than 30000.

while starting_fuel_level < 5000 or starting_fuel_level > 30000:
    if starting_fuel_level < 5000:
        starting_fuel_level = int(input("Fuel Level Too Low (Minimum of 5001) - Enter new starting fuel level: "))
    elif starting_fuel_level > 30000:
        starting_fuel_level = int(input("Fuel Level Too High (Maximum of 30,000) - Enter new starting fuel level: "))



# b. Use a second loop to query the user for the number of astronauts (up to a maximum of 7). Validate the entry.
while astros_onboard <= 0 or astros_onboard > 7:
    astros_onboard = int(input("Error: Crew Size Can Only Be Between 1-7 - Readjust and enter new crew number: "))

# c. Use a final loop to monitor the fuel status and the altitude of the shuttle. Each iteration, decrease the fuel level by 100 units for each astronaut aboard. Also, increase the altitude by 50 kilometers.
while starting_fuel_level > (100*astros_onboard):
    starting_fuel_level -= (100 * astros_onboard)
    altitude += 50
print(f"The shuttle gained an altitude of {altitude} km and has {starting_fuel_level} kg of fuel left.")

# Exercise #2: Print the result with the phrase, The shuttle gained an altitude of ___ km and has ___ kg of fuel left. Fill in the blanks with the altitude and fuel level values.
if altitude >= 2000:
    print("Orbit Achieved!")
else:
    print("Failed to reach Orbit.")
# If the altitude is 2000 km or higher, add “Orbit achieved!” Otherwise add, “Failed to reach orbit.”

Example output:
Enter starting fuel level: 7004
Enter astros onboard level: 6
The shuttle gained an altitude of 550 km and has 404 kg of fuel left.
Failed to reach Orbit.