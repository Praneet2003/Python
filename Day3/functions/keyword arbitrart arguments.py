def average(*number):
    sum = 0
    for i in number:
        sum = sum+i
    print("The averae of numers is :",sum/len(number))
average(10,20,30)