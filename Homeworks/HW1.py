#Question 1

#Generating a 3x3 matrix with 9 random prime numbers (using the for loop)

A=[[[] for i in range(3)] for i in range(3)]
for i in range(3):
    for j in range(3):
        number=int(input("Please Enter Elements of Matrix A:")) 
        A[i][j]=number
        print(A)

        
