import requests
import pickle
import numpy as np

url= "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
data= requests.get(url)
final=data.text
lines=[]
# for line in final:
#     lines.append(line.split(" \n "))
# lines.append(final.split("\n"))

# /////this is using numpy funciton
final1=np.char.splitlines(final)
print(final1)
# print(lines)


# ///////starting the pickling of the list
# file_name="86_test11.1_pickle_irus.pkl"
# fileobj=open(file_name,"wb")
# # url1=pickle.dump(lines,fileobj)
# /////////////this is not working because some thing is a problem
# url1=pickle.dump(final,fileobj)
# fileobj.close()
# print(data)

# //////stating the decode of the file
file_name="86_test11.1_pickle_irus.pkl"
fileobj= open(file_name, "rb")
url2= pickle.load(fileobj)
print(url2)
