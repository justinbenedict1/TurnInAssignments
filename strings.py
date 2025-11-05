# ---- Exercise 2: Bracket Notation Basics ----

text = 'Strings_are_sequences_of_characters.'
word = 'tomato'

# 1. Print a slice of the first 12 characters from 'text'.
print(text[0 : 12])

# 2. Print a slice of the last 12 characters from 'text'. You should NOT have to count the index values yourself!
print(text[-12:])


# 3. Print a slice of the middle 12 characters from 'text'.
len_text = len(text)
hp = (len_text/2)
print(text[int(hp) - 6 : int(hp) + 6])

# ---- Exercise 3: Looping Through a String ----

# Use index values to loop backwards through 'word'.

# 1. Print 1 letter per line.
max_index = (len(word)-1)
for index in range(max_index, -1, -1):
    print(word[index])


# 2. Refactor the code to use the accumulator pattern to build up and print the reversed string. For example, if given 'good', print 'doog' on one line.
Given_Word = input("Enter a word that you would like reversed: ")
rGiven_Word = ""
Given_Word_Mindex = (len(Given_Word)-1)
for index in range(Given_Word_Mindex, -1, -1):
    rGiven_Word = rGiven_Word + Given_Word[index]

print(rGiven_Word)
# 3. Refactor the code to print a combination of the original and reversed string. For example, given 'tomato', print 'tomatootamot'. (If you want to be fancy, print 'tomato | otamot').
Given_Word = input("Enter a word that you would like reversed: ")
rGiven_Word = ""
Given_Word_Mindex = (len(Given_Word)-1)
for index in range(Given_Word_Mindex, -1, -1):
    rGiven_Word = rGiven_Word + Given_Word[index]

print(Given_Word, "|", rGiven_Word)