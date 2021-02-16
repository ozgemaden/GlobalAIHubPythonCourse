#Explain your work

#Question 1

A=[[[] for i in range(3)] for i in range(3)]
for i in range(3):
    for j in range(3):
        number=int(input("Please Enter Elements of Matrix A:")) 
        A[i][j]=number
        print(A)
