# //////regular expresion///////////regex expresions
# ///// this is basicaaly use to search or other feachers to help in machine learning and data science
# /////many tools to use the search or splits the string file 
# ////for example we write a very big data and than we want to chk or retrive just one work than we use this tool
# //// these tools are "findall, search, split, sub, finditer"
# ////in this tutorial we use just finditer function
# /////////////mata charactors
# ////this is the list which we use in the regular expresions
# 1- []---- A set of charactors
# 2- \-----signals a specal sequance(can also be used to escspe special charactors)
# 3- . ----any charactor(expect newline character) 
# 4- ^ ----stats with (this function is use to chk the first work :)
# 5- $ ----Ends with (this function is use to check the last work )\
# 6- * ----zero or more occrance (it is chk that first of all we input the number than next word chack that who many words are exists there) 
# 7- + ----one or more occrance (first of all we input a number than next num check that how many works or numbers are exits it)
# 8- {}----exactly the specified number of occurance (in this function we use {} first num is as a input and that if we want to that exactly how many numbers or words exists it) 
# 9- | ----either or (this function is use to 2 or more words to chk that exists or not)
# 10- ()---capture and group 


# /////////////spacial charactos
# 11- \A ----returns the match if the spacified charactors are at the begging of the string
# 12- \b ----returns the match if the spacified charactors are at the begging or at the end of the string
# 13- \B ----returns the match if the spacified charactor are present but not at the begging or at the end of the sting
# 14- \d ----returns the match where the string contains digit (numbers from 0-9)
# 15- \D ----return the match where the string dost not contains digit
# 16- \s ----return the match where the string contains a white space charactors
# 17- \S ----returns the match where the string does not contains a white space charactors
# 18- \w ----returns the match where the string contain the word charactors
# 19- \W ----returns the match where the string does not contains the word charactors
# 20- \Z ----returns the match if the spacified charactors are at the end of the string

# ////////first of all we import the re module 
# ////// re means the regular expresions in python
 
import re

data= """Tata Motors Group (Tata Motors) is a $35 billion organisation. It is a leading global automobile manufacturing company. Its diverse portfolio includes an extensive range of cars, sports utility vehicles, trucks, buses and defence vehicles. Tata Motors is one of India's largest OEMs offering an extensive range of integrated, smart and e-mobility solutions""" 

# //////r means the row string this is use to ignore the excape sequance charactors
# //////compile is a function
# /////finditer is also a function of regular expressions
# patt = re.compile(r'smart')
# /////////dot(. means a any charactor)
# patt = re.compile(r'.')
# patt = re.compile(r'.Tata')
# //////^ starting string
# patt = re.compile(r'^Tata')
# ////////$ end of the string
# patt = re.compile(r'Tata$')
# patt = re.compile(r'ons$')
# //// using * 0 to many charactors
# patt = re.compile(r'ons*')
# //////+ min one to many charactors
# patt = re.compile(r'ons+')
#  /////////{} exatly numbers or charctors
# patt = re.compile(r'in{1}')
# /////() this is use the group
# patt = re.compile(r'(in){1}')
# //////// | this is the or means that given one or more words which we type
# patt = re.compile(r'in{1}|on')


# //////////////////spacial sequance
# patt = re.compile(r'\ATata')
patt = re.compile(r'\bTata')
matches=patt.finditer(data)
for i in matches:
    print(i)
    # print(data[326:331])