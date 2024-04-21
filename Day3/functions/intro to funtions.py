# Functions :-
# it is a block of statement which performes a specific task when called.
# Functions are of two types:-
# 1:) Built-in Functions:- These functions are defined and pre-coded in python.
# Eg:- min(),max(),len(),range(),sum(),type(),dict(),list(),tuple() etc.
x = (1,2,3,4,5,6)
res = sum(x)
print(res)
# 2:) User-defined Functions:- we can create a functions a/c to our needs,such functions are called user defined functions.
# SYNTAX:-
def gmean(a,b):
    mean = (a*b)/(a+b)
    return mean
a=gmean(5,6)
print(a)