my_string = "LaunchCode"

# a) Use string methods to remove the first three characters from the string and add them to the end.

to_be_moved = my_string[0 : 3]           # Grab the first three letters ("Lau") and store them
my_string = my_string[3:] + to_be_moved  # Take everything from index 3 onward and add "Lau" to the end
print(my_string)                         # Prints "nchCodeLau"


# Use a template literal to print the original and modified string in a descriptive phrase.

my_o_string = 'LaunchCode'                 # Store the original word
to_be_moved = my_o_string[0 : 3]           # Grab the first three letters again
my_string = my_o_string[3:] + to_be_moved  # Create the modified version
print(my_string)                           # Print the modified string
print(my_o_string)                         # Print the original string for comparison


# b) Modify your code to accept user input. Query the user to enter the number of letters that will be relocated.

my_string = input("Enter a word to test: ")                 # Ask user to type a word
remove_from_index = int(input("Enter a number to test: "))  # Ask user how many letters to move; convert from string to int
to_be_moved = my_string[0 : remove_from_index]              # Grab the number of letters they asked for
my_string = my_string[remove_from_index:] + to_be_moved     # Move those letters to the end
print(my_string)                                            # Print the new word


# c) Add validation to your code to deal with user inputs that are longer than the word.
# In such cases, default to moving 3 characters. Also, the template literal should note the error.

my_string = input("Enter a word to test: ")                 # Ask user for a word again
remove_from_index = int(input("Enter a number to test: "))  # Ask user how many letters to move
if remove_from_index >= len(my_string):                     # Check if the number is too big
    remove_from_index = 3                                   # If so, reset it to 3
    print("The number entered was longer than the highest possible number, the value has been set to 3.")
to_be_moved = my_string[0 : remove_from_index]               # Grab the letters to move
my_string = my_string[remove_from_index:] + to_be_moved     # Create the modified version
print(my_string)                                             # Print the final transformed string
