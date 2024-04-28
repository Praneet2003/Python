# Formula for calculating the no of white spaces:-
# No of whitespace = no of rows - row.no
rows = int(input("Enter the no of rows: "))
for i in range(1,rows+1,1):
    for j in range(1,i+1):
        print("*",end=' ')
    print(' ')
for k in range(rows-1,0,-1):
    for h in range(1,k+1):
        print("*",end=' ')
    print(' ')
        
        