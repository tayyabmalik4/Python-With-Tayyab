print("Welcome to the calcculator")
num1 = int(input("enter your first value: "))
num2 = int(input("enter your secend value: "))

print("Enter your operator" , "+" ,"-" , "*" , "/")
op = input()

if op=="+":
        if num1==56 and num2==9:
                print("77")
        else:
                num3 = num1+num2
                print(num3)

elif op=='-':
        num3 = num1-num2
        print(num3)

elif op=='*':
        if num1==45 and num2==3:
                print(555)
        else:
                num3=(num1*num2)
                print(num3)

elif op=='/':
        if num1==56 and num2 ==6:
                print(4)
        else:
                num3=num1/num2 
                print(num3)  

else:
        print("your value is invalid")





