# Strings:- It is like an array of chacter in python.
# string are written in "xyz" or 'xyx'
# for multiple line string we either use single triple quotes or triple double quotes
# '''xyz''' or """xyz"""
str1 = '''hey!
    i am praneet raj
    and i am 21 years old.'''
print(str1)
for characters in str1:
    print(characters)
str2 = """HEllo world
    Currently i am learning Strings
    in python."""
print("\n",str2)
print("printed by using loop\n")
for character in str2:
    print(character ,sep=" " ,end="")