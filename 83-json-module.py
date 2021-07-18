# /////////////this is the json module tutorial/////////////////////
# this is the json module defintion-------------The full-form of JSON is JavaScript Object Notation. It means that a script (executable) file which is made of text in a programming language, is used to store and transfer the data. Python supports JSON through a built-in package called json. To use this feature, we import the json package in Python script. The text in JSON is done through quoted-string which contains the value in key-value mapping within { }. It is similar to the dictionary in Python.
# /////////the full form of json module is: javascript Object Notation module and it is helpful in web applications and it is very important for all the purposes
# ///////if we want to add the data throgh json than we use json.loads and it helps to retrive the data and very helpful
# ///////we use this module but this work is complited manully but we don't handle it as a manully /
# ////for example if we print just one part than at the help of json.loads function we can do this but munally we are not working at the same condition and so one
# /////if we want to convert the python list or dictionary to json cormat than we use json.dump() function 
# //// it use the function to pretty the all data and this is very helpful function
import json

# data= '{"tayyab":"AI developer","wish":"i want to build a AI in future inshaAllah"}'
# # ///////this is the manully
# print(data)
# # this is print as the use of json.loads function
# AI=json.loads(data)
# print(AI)
# print(AI["wish"])


# ////////////////// this is start the json.dump function////////////
# data2={
#     "name":"Tayyab Malik",
#     "frends":["junaid","zahid","uzair","zaheer","mohsin"],
#     "brothers":("kamran","ahmad","kashif"),
#     "job":["i will achive the job in AI as soon as possible",False]
# }
# print(data2)
# AI2=json.dumps(data2)
# print(AI2)


# ////starting json.load module
# /////this is the definition of json.load() function----------------json.load() takes a file object and returns the json object. A JSON object contains data in the form of key/value pair. The keys are strings and the values are the JSON types. Keys and values are separated by a colon. Each entry (key/value pair) is separated by a comma.
# ////first of all we creat a file which json type and than we creat a values and than import the values by the help of open function
# ///than use json.load() function and than use for loop to itrate the vales and then print it 

# f=open("83-json-module-load.py")
# # print(f.read())
# # ///////using json.load() function
# AI3=json.load(f)
# # print(AI3)
# for i in AI3["emp_details"]:
#     print(i)
# f.close()


# //////////sort keys in dumps \\\\\\\\\
# ///////this function is use to sorting the key value pairs in python by Alphabatically order
# ///////this is the definotion of the sort keys in dumps function------------Dumping JSON serializes a JSON object to string format for printing. Sorting the keys when dumping saves the key-value pairs in alphabetical order by keys.
# /////this is the extra function of json.dumps and it is use to sorting the values Alphabatically order


data2={
    "name":"Tayyab Malik",
    "frends":["junaid","zahid","uzair","zaheer","mohsin"],
    "brothers":("kamran","ahmad","kashif"),
    "job":["i will achive the job in AI as soon as possible",False]
}
print(data2)
AI2=json.dumps(data2, sort_keys=True)
print(AI2)