# Capitalize
txt = "hello"
x = txt.capitalize()
print (x)

# Lowecase --- Casefold
txt1 = "Hello1"
x = txt1.casefold()
print(x)

# Centeralized the text
txt2 = "banana"
x = txt2.center(20)  # give 20 space
print(x)

# Count how many times specific word use in text
txt3 = "I love apples, apple are my favorite fruit"
x = txt3.count("apple") # specific word
print(x)

# 10 start value and 24 ending value b/w them how many time particular word use
txt5 = "I love apples, apple are my favorite fruit"
x = txt5.count("apple", 10, 24)
print(x)

# End with particular ending or not
txt6 = "Hello, welcome to my world."
x = txt6.endswith("my world.")
print(x)

# Start with 5 and ends on 11 End with particular ending or not 
txt = "Hello, welcome to my world."
x = txt.endswith("my world.", 5, 11)
print(x)

# The find() method finds the first occurrence index value of the specified word.
# The find() method returns -1 if the value is not found.
txt7 = "Hello, welcome to my world."
x = txt7.find("e")   # txt7.find("e", 5, 10)
print(x)

#The rfind() method finds the last occurrence of the specified value.
#The rfind() method returns -1 if the value is not found.
#The rfind() method is almost the same as the rindex() method.
txt18 = "Mi casa, su casa."
x = txt18.rfind("casa")
print(x)

#The index() method finds the first occurrence of the specified value.
#The index() method raises an exception if the value is not found.

#The index() method is almost the same as the find() method, the only difference 
# is that the find() method returns -1 if the value is not found.

txt8 = "Hello, welcome to my world."
x = txt8.index("welcome")     #  txt8.index("welocome", 5, 10)
print(x)

#The rindex() method finds the last occurrence of the specified value.
#The rindex() method raises an exception if the value is not found.
#The rindex() method is almost the same as the rfind() method.
txt19 = "Mi casa, su casa."
x = txt19.rindex("casa")
print(x)

#The isalnum() method returns True if all the characters are alphanumeric, 
#meaning alphabet letter (a-z) and numbers (0-9)
txt9 = "Company 12"
x = txt9.isalnum()
print(x)

# The isalpha() method returns True if all the characters are alphabet letters
txt10 = "Company10"
x = txt10.isalpha()
print(x)

#The isdecimal() method returns True if all the characters are decimals (0-9).
txt11 = "1234"
x = txt11.isdecimal()
print(x)

# isdigit() method returns True if all the characters are digits, otherwise False.
txt12 = "50800"
x = txt12.isdigit()
print(x)

#The isnumeric() method returns True if all the characters are numeric (0-9)
txt14 = "565543"
x = txt14.isnumeric()
print(x)

#The islower() method returns True if all the characters are in lower case
txt13 = "hello world!"
x = txt13.islower()
print(x)

# The isupper() method returns True if all the characters are in upper case
txt15 = "THIS IS NOW!"
x = txt15.isupper()
print(x)

#The replace() method replaces a specified phrase with another specified phrase
txt17 = "I like bananas"
x = txt17.replace("bananas", "apples")
print(x)

#The startswith() method returns True if the string starts with the 
# specified value, otherwise False.
txt20 = "Hello, welcome to my world."
x = txt20.startswith("Hello")
print(x)

# The swapcase() method returns a string where all the upper case letters are 
#lower case and vice versa.
txt21 = "Hello My Name Is PETER"
x = txt21.swapcase()
print(x)

#The title() method returns a string where the first character in every word 
# is upper case.
txt22 = "Welcome to my world"
x = txt22.title()
print(x)

#The upper() method returns a string where all characters are in upper case.
txt23 = "Hello my friends"
x = txt23.upper()
print(x)

# The lower() method returns a string where all characters are lower case.
txt16 = "Hello my FRIENDS"
x = txt16.lower()
print(x)

#split() split the string
txt24 = "Hello my FRIENDS"
x = txt24.split()
print(x)
