food = "water bottles,meal packs,snacks,chocolate"
equipment = "space suits,jet packs,tool belts,thermal detonators"
pets = "parrots,cats,moose,alien eggs"
sleep_aids = "blankets,pillows,eyepatches,alarm clocks"

# a) Use split to convert the strings into four cabinet lists. Alphabetize the contents of each cabinet.
cabinet1 = food.split(",")
cabinet1 = sorted(cabinet1)

cabinet2 = equipment.split(",")
cabinet2 = sorted(cabinet2)

cabinet3 = pets.split(",")
cabinet3 = sorted(cabinet3)

cabinet4 = sleep_aids.split(",")
cabinet4 = sorted(cabinet4)


# b) Initialize a cargo_hold list and add the cabinet lists to it. Print cargo_hold to verify its structure.
cargo_hold = [cabinet1, cabinet2, cabinet3, cabinet4]
print(cargo_hold)

# c) Query the user to select a cabinet (0 - 3) in the cargo_hold.
selected_cabin = int(input("Enter a cabinet number (1-4): "))
# d) Use bracket notation and format to display the contents of the selected cabinet. If the user entered an invalid number, print an error message.


while selected_cabin not in [1, 2, 3, 4]:
    selected_cabin = int(input("ERROR: Enter a cabinet number (1-4): "))

print(cargo_hold[selected_cabin - 1])




# e) Modify the code to query the user for BOTH a cabinet in cargo_hold AND a particular item. Use the in method to check if the cabinet contains the selected item, then print “Cabinet ____ DOES/DOES NOT contain ____.”
selected_cabin = int(input("Enter a cabinet number (1-4): "))
selected_item = input("Enter an item name: ")

while selected_cabin not in [1, 2, 3, 4]:
    selected_cabin = int(input("ERROR: Enter a cabinet number (1-4): "))

print(cargo_hold[selected_cabin - 1])

while selected_item not in cargo_hold[selected_cabin - 1]:
    print("ERROR: Item not in cabinet")
    selected_item = input("Enter another item: ")

print(f"{selected_item} found in Cabinet {selected_cabin}!")


