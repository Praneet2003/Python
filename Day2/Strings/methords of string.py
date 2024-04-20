# Methods of Strings:-
# Note:- String are immutable, hence all methord give anew string after the operations

# 1:) upper():- Converts all characters of string to uppercase
# Eg:- 
a = "Apple"
print(a.upper())

# 2:) lower():- Converts all characters of string to lowercase
print(a.lower())

# 3:) replace():- Replaces all occurence of previous string with other string
# Eg:-
print(a.replace("Apple","Banana"))

# 4:) rstrip():- This method removes any tralling character which is after the string.
x = "!!!!! Hello !!!!!"
print(x.rstrip("!"))# Output: !!!!! Hello

# 5:) split():- This method return the seperated strings as list items
# Eg:-
friends = "Praneet Mehul Ayush"
print(friends.split(' '))#Output: ['Praneet', 'Mehul', 'Ayush']

# 6:) Capitalize():- It is used to Change the first charcater of words in a string to the upper case and rest to the lowercase
#eg:-
c = "hello world"
print(c.capitalize()) #Output:- Hello world

#7:) Center():- Allings the whole string to the center of the consle
#Eg:-
d = "Hello world"
print(d.center(20," "))# Synatx:- center(length to be shifted, with what to skip)

#8:) Count():- This method returns the number to times the given value has occured with the given string.
# Eg:-
print(d.count("H"))

# 9:) endswith():- This method checks whether the str end with a given value or not
# Eg:-
y = "Welcome to the console !"
print(y.endswith("!"))#Output: True

# 10:) find():- THe method search for the occurence of the given value, if it is present the it returns the index of the given value, 
#              else if it is not present then it return -1.
# Eg:-
str = "He's name is  \"Praneet\",and he is 20 years old.\n"
print(str.find("is"))

# 11:) index():- This method is similar to find() but if the value is absent then it return error
# eg:-
# print(str.index("Harry")) # it gives an errror because Harry is not present in the str

# 12:) isalnum() :- This method return True if the entire string consits of a-z,A-Z,0-9, if not it returns False
# Eg:-
str1 = "Welcome To Console" # koi vi specical char nhi chahiye yha tk ki space vi problem krta hai.
print(str1.isalnum()) 

# 13:) isalpha():- This method return True if the entire string consits of a-z,A-Z if not it returns False
# Eg:-
print(str1.isalpha())

# 14:) islower():- If all characters of strings are lowercase then it gives True, else returns False
# Eg:-
print(c.islower()) # Output:True

# 15:) isprintable():- This method Returns True if all the given values within the string are printable, else it return False.
# Eg:- 
print(str1.isprintable()) #Output: True
print(str.isprintable())# Output: False
# 16:) isspace():- If only space is available then it return True, else return False.
# Eg:-
e = "Hel   l  o"
f = "       "
print(e.isspace()) #False
print(f.isspace()) #True

# 17:) istitle():- It returns True only if first letter of every word in string is Capitalized, else it returns false.
# Eg:-
print(str1.istitle())# True

# 18:) isupper():- if all characters of a strings are in Uppercase then it returns True, else returns False
# Eg:-
name = "P R A N E E T"
print(name.isupper()) #True

# 19:) startswith():- it check that whether a string starts with the given value or not 
# Eg:-
g = "Python Hello World"
print(g.startswith("P"))#True

# 20:) title():- It Capitalize all the first characters of words in the srting
# Eg:-
print(str.title())