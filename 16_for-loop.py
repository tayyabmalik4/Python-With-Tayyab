# list = ["tayyab", "junaid", "zahid", "channoski"]
# list = [["tayyab",2], ["junaid",3], ["zahid",3], ["channoski",5]]
# for item, lollypop in list:
#     print(item,"and the lollypop" ,lollypop)
test = ["int","float","junaid",3,5,7,6,8,9,44,66,77,33,66,77,88]
for item in test:
    if str(item).isnumeric() and item>6:
        print(item)