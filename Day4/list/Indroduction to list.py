# list is an ordered collection of data.
# Multiple values  are stored within a single variable.
# List itmes are stored in [] sepersted by comma.
# List are mutable.
#Eg:-
List = [20,40,50,"Praneet","Mehul","Ayush"]
print(len(List))
for i in range(0,len(List),1):
    print(List[i])
    if(List[i]=="Mehul"):
        print("Life Changer")