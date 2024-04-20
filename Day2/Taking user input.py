# Taking input from user:-
a = input("enter the value of a: ")
print(type(a))#<class 'str'>
# BY default the input taken from user is in string data type so we will use typeCasting here
a = int(a)
print(type(a))#<class 'int'>
# Taking input as integer from user.......
b = int(input("enter the value of b: "))
c = input("Enter the operator: ")
# Desigining a simple calulator for user:
sum = a+b
sub = a-b
mul = a*b
div = a/b
floor_div = a//b
if(c == '+'):
    print(sum)
elif(c =='-'):
    print(sub)
elif(c == '*'):
    print(mul)
elif(c=='/'):
    print(div)
elif(c=='//'):
    print(floor_div)
else:
    print("Invalid Oerator")
