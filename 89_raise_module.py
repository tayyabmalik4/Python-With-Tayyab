# this is the python buildin module
# this is use without import 
# the main purpose of the raise module is to handle the errors for very starting which is gaining the time 
# for many error handling functions in this module for example ------ 
# this is the website link where all the detail is exists it ----------https://docs.python.org/3/library/exceptions.html
# (1)-raise Exception ---------------
# (2)- Arithmatic---------------
# (3)- Buffor Error---------------
# (4)- LookUp Error---------------
# (5)- AssertionError---------------Raised when an assert statement fails.
# (6)-attributeError---------------
# (7)-EOFError(End of file)---------------Raised when the input() function hits an end-of-file condition (EOF) without reading any data. (N.B.: the io.IOBase.read() and io.IOBase.readline() methods return an empty string when they hit EOF.)
# (8)-Flotting point Error---------------
# (9)-generatorExit---------------
# (10)-EmportError---------------
# (11)-ModuleNoFoundError---------------A subclass of ImportError which is raised by import when a module could not be located. It is also raised when None is found in sys.modules.
# (12)-IndexError---------------
# (13)-KeyError---------------
# (14)-KeyboardInterrup
# (15)-Memoryerror---------------
# (16)-NameError---------------Raised when a local or global name is not found. This applies only to unqualified names. The associated value is an error message that includes the name that could not be found.
# (17)-NotImplementedError---------------
# (18)- OSError---------------
# (19)-OverflowError---------------
# (20)-RecursionError---------------
# (21)-RefranceError---------------
# (22)-RuntimeError---------------
# (23)-StopItration---------------
# (24)-SyntexError---------------
# (25)-IndentationError---------------
# (26)-TabError---------------
# (27)- SystemError---------------
# (28)- SystemExit---------------
# (29)- TypeError---------------
# (30)-UnboundLocalError---------------
# (31)- UnicodeError---------------
# (32)-UnicodeEncodeError---------------
# (33)-UnicodedecodeError---------------
# (34)-UnicodeTranslateError---------------
# (35)-ValueError---------------
# (36)-ZeroDivisionError---------------
# (37)-Environmenterror---------------
# (38)-IOError---------------
# (39)-WindowsError---------------
# (40)- BlockingIOError---------------
# (41)-ChildProcessError---------------
# (42)-ConnectionError---------------
# (43)- BrokenPipeError---------------
# (44)- connectionAbortedError---------------
# (45)- ConnectionRefusedError---------------
# (46)- ConnectionResetError---------------
# (47)- FileExistsError---------------
# (48)-FileNotFoundError---------------
# (49)- InterruptedError ---------------
# (50)-IsADirectoryError---------------
# (51)-NorADirectoryError---------------
# (52)-Permissionerror---------------
# (53)-ProcessLookupError---------------
# (54)-Timeouterror---------------
# ()-///////////////////Warnings
# (1)-Warning---------------
# (2)-UserWarning---------------
# (3)-DeprecationWaring---------------
# (4)-PendingDeprecarionWaring---------------
# (5)-SyntaxWarning---------------
# (6)-RuntimeWarning---------------
# (7)-FutureWarning---------------
# (8)-ImportWarning---------------
# (9)-UnicodeWarning---------------
# (10)-BytesWarning---------------
# (11)-ResourceWarnihn---------------
#
#  
#  assertion Error Definition-------------Python's assert statement is a debugging aid that tests a condition. If the condition is true, it does nothing and your program just continues to execute. But if the assert condition evaluates to false, it raises an AssertionError exception with an optional error message.


# a= input("what is your name:  ")

# if a.isnumeric():
#     raise Exception("Number are not allowed ")
# print(f"Hello {a}")

# ////1000 lines taking 1 houe

# //////use zeroDivisionError
# a=input("Enter your name")
# b=input("how much do you earn")
# if int(b)==0:
#     raise ZeroDivisionError("b is 0 so stopping the program")
# if a.isnumeric():
#     raise Exception("Numbers are not allowed")
# print(a)
# ///////////there are handles 2 raise module 
c=input()
try:
    print(a)
except Exception as e:
    if c=="tayyab":
        raise ValueError("Tayyab is blocked he is not allowed")
    print("Exception Handled")