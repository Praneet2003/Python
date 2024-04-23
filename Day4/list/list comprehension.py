# list comprehension is used to make new list from other iterables 
# such as:- list,tuples,strings,set,dictonary and even from array.

# SYNTAX:- 
# list = [<Expression> for item in items in iterables if(condition)]
# Eg:-
# print natural numbers from 1 to 50:-
naturalNo = [i for i in range(51)]
print(naturalNo)
print("\n")

# Printing the square of no's from 0 to 10
squared = [item*item for item in naturalNo if(item<11)]
print(squared)
print("\n")

# Acessing the values from squared list which is divisible by 4:
divisibleby4 = [j for j in squared if(j%4==0)]
print(divisibleby4)