import time
#in this tutorial we use 3 types of time function one is time.time() 2nd for time.asctime(time.localtime(time.time()))and 3rd for time.sleep(2)

initial = time.time()
k=0
while(k<10):
    print("this is while loop")
    k=k+1
    time.sleep(2)
print(f"While loop ran in {time.time()-initial} Secends")
# for i in range(10):
#     print("this is for loop")
# print(f"For loop ran in {time.time()-initial} Secends")

# localtime = time.asctime(time.localtime(time.time()))
# print(localtime)