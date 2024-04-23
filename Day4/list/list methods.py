# 1:)append:- used ot add items to the list.
# Eg:-
l = [1,8,94,5,6,0,54]
l.append(8)
print(l)

# 2:) sort():- used to align the list items in ascending order.
# it can't align differnt data types. 
l.sort()
print(l)
# to align list item in descending order ,we use reverse = True
l.sort(reverse=True)
print(l)

# 3:) reverse():- used to reverse the whole string no matter the orders.
# Eg:-
l.reverse()
print(l)

# 4:) index():- this method returns the first occurence of the list item.
# Eg:- 
print(l.index(8))

# 5:) count():- this method counts the no of times an item is thier in a list.
print(l.count(8))

# 6:) copy():- this function returns copy of the is list, this can be done to performe operations on the list without modifying the orignal list.
#eg:-
m = l.copy() # m = l if i do like this then the original will also be changed. 
m[0] = 6
print(l)
print(m)

# 7:) insert():- this method is used to insert an item at a given index,user has to specify the index and the item to be inserted within the index.
# SYNTAX:- <list_name>.insert(<index>,<item>)
# eg:-
l.insert(1,899)
print(l)

# 8:) extend():- this method is used to add an entire list or other collection of datatype(set,tupe,dictionary) to an existing list.
# Eg:- 
l.extend(m)
print(l)# all items of list m is now added to list l.

# Concatination of lists:-
k =l+m+l
print(k)