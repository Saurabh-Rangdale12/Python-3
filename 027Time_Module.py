import time
# sec = time.time()
# print("seconds since epoch =" , sec)
# # time.asctime()
#
# k = 0
# while(k<10):
#     print("This is while loop")
#     k+=1
# print("While Loop ran in", time.time() - sec, "Seconds")
#
# sec2 = time.time()
for i in range(10):
    print("This is For Loop")
    time.sleep(2)  # it will run following code after 2 sec
# print("For Loop ran in ", time.time() - sec2, "Seconds")

# loc0ltime = time.asctime(time.localtime(time.time()))
# print(loc0ltime) # Print local time i.e now time
