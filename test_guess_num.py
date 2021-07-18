# this is the guess excercise
print("you are just 9 items. if you choose correct ans than you win the game other wise you loose the game: \n")


i=1
while(i<=9):
    num = int(input("enter the number \n"))
    if num<59:
        if i==9:
            print("You Loose and game over")
            break
        else:
            print("you entered a less num please choose the big num,you attamps the choose num =>", 9-i)
    elif (num>59):
        if i==9:
            print("You Loose and game over")
            break
        else:
            print("you entered a greter num please write a small num,lift the choose num =>",9-i)
            
    elif (num==59):
        print("you win the game")
        break
    else:
        print("invalid value")
    i=i+1