def fun1():
    x = 100
    def fun2():
        nonlocal x
        x = 200
    print('before calling fun2:'+str(x))
    print("Calling fun2 now:")
    fun2()
    print("After calling fun2:"+str(x))

x = 50
fun1()
print("x in main:"+str(x))
