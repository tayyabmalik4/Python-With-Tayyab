# __name__is mean the main if we use name in existing file which we use function then return main otherwise return file name
# and __name__ function is use when we import file and in the file where we import file we use functions and wish not print the achual file
#////////////definition/////////////// If you import this script as a module in another script, the __name__ is set to the name of the script/module. Python files can act as either reusable modules, or as standalone programs. if __name__ == “main”: is used to execute some code only if the file was run directly, and not imported.
def printhar(string):
    return f"this is the harry python channal    {string}"
def add(a,b):
    return a+b+5
print("and the name is achully means that", __name__)
if __name__=='__main__':
    print(printhar("codewithharry"))
    o=add(5,7)
    print(o)