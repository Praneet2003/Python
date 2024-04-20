# Match case:- 
# It is simalar to switch case in c & c++
x = int(input("Enter th value of x: "))
match x:
    case 0:
        print("X is Zero")
    case 1:
        print("X is 1")
    case 2:
        print("X is 2")
    case 3:
        print("X is 3")
    case _: #default
        print("This is in the default case")
# Note:-
# 1:) here it is no more nedded to use break statements , if one condintion runs then it comes out of the match.
# 2:) If any of the cases doesn't match then defalut case runs. 