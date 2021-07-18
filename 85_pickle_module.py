# //////////////pickle module in python///////////////////////
# //////this is not for recomend because if the file is encripted and somw time later the python version is changed than we face some problems
# ////this is the build in moduile
# ////the main work of the pickle is decode of any object
# ////basically if we want to decode any object than we use picklw moduile
# ////for encoding any object than we use pickle.dump
# ////pickle.dump take 2 objects first is the object and 2nd is the fileobj 
# ////in file object use open function then it is also take 2 object 1st file name and 2nd is wb means writebinary
# ////wb means the writing binary 
# ////when we use w in IO file its mean new file is created and write the data and if the data is already present than override the data which we input

# ////and when we want to decode of the file or our code then we use pickle.load(file_name)
# ///first of all it take a file name
# ////than fileobject is take 2 objects first file name and 2nd is rb and rb means read binary
# ////than we use pickle.load() funtcion to decode the file or data and print it


# /////////pickle.loads() function 

import pickle

# languages=["python","php","HTML","CSS","JavaScript","C++","c#","ruby with rails","pandas","sk-learn","tanserflow","Numpy","keras"]
# # lan1="this is the pickle module tutorial in python"
# # # print(languages)
# # # print(type(languages))
# file_name="85_languages.pkl"
# fileobj=open(file_name,"wb")
# l=pickle.dump(languages,fileobj)
# # l1=pickle.dump(lan1,fileobj)
# fileobj.close()


# //////starting to decode of the file or program
# file_name="85_languages.pkl"
# fileobj=open(file_name,"rb")
# lan=pickle.load(fileobj)
# print(lan)


# //////now we describe the pickle.loads() function in python


