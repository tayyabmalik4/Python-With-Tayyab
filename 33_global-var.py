# l=10 #global variable ----this is not for change and just read it---if you have change the global varialbe value than use --global keyword=> "global" in the function

# def function1(n):
#     l=5 #local variable----this is change and also read in just function
#     m=8
#     # global l 
#     l=l+45
#     print(l,m)
#     print(n,"I have printed ")
# function1("This is me")
# print(l)


x=89
def harry():
    x=20
    def rohan():
        global x
        x=88
    # print("before calling roahn() ",x)
    rohan()
    print("after calling rohan()", x)

harry()
print(x)