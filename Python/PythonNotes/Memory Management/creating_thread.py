from threading import Thread
# def disp():
#     print("Thead Running")

# t=Thread(target=disp)
# t.start()


# def disp(a):
#     print("Thead Running",a)

# t=Thread(target=disp,args=(10,))
# t.start()




# t=Thread(target=disp,args=(10,20))
# t.start()
def disp(a,b):
    print("Thead Running ", a, b)

for i  in range(5):
    t=Thread(target=disp,args=(10,20))
    t.start()