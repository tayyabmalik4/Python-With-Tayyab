# this is the test of pattern printing

# print("Enter the number: ")
# n=int(input())
# print("Enter the 0 or 1")
# b = int(input())
# chk = bool(b)
# if chk==True:
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print("*", end=" ")
#         print()
# elif chk==False:
#     for i in range(n,0,-1):
#         for j in range(1,i+1):
#             print("*",end=" ")
#         print()
def number():
    n = int(input("enter the number: "))
    b = int(input("Enter the 0 or 1: "))
    # chk = bool(b)
    if b ==1:
        for i in range(1,n+1):
            print(i*"*")

    elif b==0:
        # there are 2 ways to solve it--- and range 3rd value is use to ulat the pattern
        for i in range(n,0,-1):
            print(i*"*")
        # for i in range(1,n+1):
            # print(n*"*")
            # n = n-1
    else:
        print("You entered a wrong number please select a corect number 0 or 1")

    print("if you have start again then press y if you have not started then press any key to exit")
    again = input("yes or no: ")
    if (again=="y"):
        number()
    else:
        print("thank you!")

number()

