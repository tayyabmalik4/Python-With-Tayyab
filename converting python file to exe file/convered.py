# //////////////converd the python file to exe file by using pyinstaller module
# ////////first of all install pyinstaller using pip ------------pip install pyinstaller
# //////////than use this command--------------------pyinstaller filename
# ///////if module is not working than we go to this the path and copy the path and paste the environment variable in path
# /////// the full path is--------------C:\Users\%USERNAME%\AppData\Roaming\Python\Python37\Scripts

# ////////if we want to just one file of exe than we use this command -------------pyinstaller --onefile filename

data= int(input("enter 1st number:   "))
data1=int(input("enter 2nd number:   "))
result=data+data1
print("your answer is:   ",result)