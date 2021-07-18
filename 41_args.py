# def function_name_print(a,b,c,d,e):
    # print(a,b,c,d,e)

# function_name_print("tayyab", "junaid", "zahid", "uzair", "zaheer")

# this is the args tutorial and in this args we add many values in list but it is go to function as a tupal
# first of all we use normal and then args and than kwags
# kwags is use in dictionary
def fun_args(normal,*args,**kwags):
    print(normal)
    for i in args:
        print(i)
    for key,value in kwags.items():
        print(f"{key} is a {value}")
value="this is just chk it is it a normal function or not?"
names=["tayyab","junaid","zahid","uzair","zaheer"]
keys={"tayyab":"bakend","zahid":"frontend","junaid":"also fornend"}
fun_args(value,*names,**keys)