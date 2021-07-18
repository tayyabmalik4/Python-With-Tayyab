# function caching means that:
# when our program is very large or very long 
# than the code is required a time to exicuting it
# than we use function caching
# function caching basically a module who store the time when first time program is run
# the module name is 'lru_cache' and this is import the functools module
# basically this is work as a decorator
# ///////////////time.sleep//////////Python time sleep function is used to add delay in the execution of a program. We can use python sleep function to halt the execution of the program for given time in seconds. Notice that python time sleep function actually stops the execution of current thread only, not the whole program.


import time
# if we decrease the time then we use function cache
from functools import lru_cache; 
# ////////at this stage we input a values which is store the time 
@lru_cache(maxsize=2)
# some work taking n times
def time_take(n):
    time.sleep(n)
    return n

if __name__=="__main__":
    time_take(3)
    print("this function is exicuted at the 3 secends later")
    time_take(3)
    print("this is the secend part")
    time_take(5)
    print("this is the 3rd part")