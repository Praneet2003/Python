#for loop:-
# for loop can iterate over a sequence of iterable objects in python 
# Eg:-
name = "Praneet"
for i in name:
    print(i)
list1=["Praneet","mehul","Ayush"]
for b in list1:
    print(b)
    if(b=="mehul" or b =="Ayush"):
        print("Special persons")
for j in range(10):# By default it starts from 0 and end at 9
    print(j, end=" ")#print from 0 to 9
    print(j+1,end=" ")#print from 1 to 10
print("\n")
for k in range(101, 201):# starts from 101 an ends at 200
    print(k,end=" ")# print from 101 to 200
# printing all even numbers from 0 to 100
print("\n")
print("\n")
for m in range(2,101,2):
    print(m, end=" ")
print("\n")
print("\n")