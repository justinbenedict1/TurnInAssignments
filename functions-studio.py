# We want to COMPLETELY reverse a list by flipping the order of the entries AND flipping the order of characters in each element.

# a) Define a 'reverse_characters' function. Give it one parameter, which will be the string to reverse.
# b) Within the function, use the 'list' function to split a string into a list of individual characters
# c) 'reverse' your new list.
# d) Use 'join' to create the reversed string and return that string from the function.
# e) Create a variable of type string to test your new function. # f) Use 'print(reverse_characters(my_variable_name))'; to call the function and verify that it correctly reverses the characters in the string.
# g) Use method chaining to reduce the lines of code within the function.
# a) Define the function
def reverse_character(string):
    if isinstance(string, str):
        char_list = list(string)
        char_list.reverse()
        reversed_string = "".join(char_list)
        return reversed_string
    elif isinstance(string, int):
        string = str(string)
        char_list = list(string)
        char_list.reverse()
        reversed_string = "".join(char_list)
        reversed_string = int(reversed_string)
        return reversed_string
    return None


test_string = "test"
test_number = 123456789

print(f"Reversed String 1: {reverse_character(test_string)}")
# Verify with a string
print(f"Original String: {test_string}")
print(f"Reversed String: {reverse_character(test_string)}")
print("\n")
# Verify
print(f"Original Number: {test_number}")
print(f"Reversed Number: {reverse_character(test_number)}")

# 2) The 'split' method does not work on numbers, but we want the function to return a number with all the digits reversed (e.g. 1234 converts to 4321 and NOT the string "4321")
# a) Add an if statement to your reverse_characters function to check the typeof the parameter.
# b - d) If type is ‘string’, return the reversed string as before. If type is ‘number’, convert the parameter to a string, reverse the characters, then convert it back into a number. Return the reversed number.
# e) Be sure to print the result returned by the function to verify that your code works for both strings and numbers. Do this before moving on to the next steps.

# 3) Create a new function with one parameter, which is the list we want to change. The function should:
# a) Define and initialize an empty list.
# b) Loop through the old list.
# c) For each element in the old list, call reverse_characters to flip the characters or digits.
# d) Add the reversed string (or number) to the list defined in part ‘a’.
# e) Return the final, reversed list.
# f) Be sure to print the results from each test case in order to verify your code.
list_test1 = ['apple', 'potato', 'Capitalized Words']
list_test2 = [123, 8897, 42, 1168, 8675309]
list_test3 = ['hello', 'world', 123, 'orange']


def reverse_character(data):
    if isinstance(data, str):
        # Reverses string characters
        char_list = list(data)
        char_list.reverse()
        return "".join(char_list)

    elif isinstance(data, int):
        # Reverses integer digits
        str_data = str(data)
        char_list = list(str_data)
        char_list.reverse()
        return int("".join(char_list))

    else:
        # Returns the element as-is if not a string or integer
        return data

def process_list(old_list):
    new_list = []

    for element in old_list:
        reversed_element = reverse_character(element)
        new_list.append(reversed_element)
    return new_list

print(f"Original List 1: {list_test1}")
result1 = process_list(list_test1)
print(f"Processed List 1: {result1}\n")
# Test Case 2 (Integers)
print(f"Original List 2: {list_test2}")
result2 = process_list(list_test2)
print(f"Processed List 2: {result2}\n")

print(f"Original List 3: {list_test3}")
result3 = process_list(list_test3)
print(f"Processed List 3: {result3}")


list_test1 = ['apple', 'potato', 'Capitalized Words']
list_test2 = [123, 8897, 42, 1168, 8675309]
list_test3 = ['hello', 'world', 123, 'orange']
