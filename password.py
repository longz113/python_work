'''
测试github是否可以
'''
print("Hello !")
n=5
while n:
    passwords=input("please input you password: ")
    password=int(passwords)
    if password==123456:
        print("You are right.\t\n"+"Please come in.")
        break
    else:
        print("You are wrong.")
        n=n-1
        print("you have "+str(n)+" times.\n")
        if n==0:
            print("Please contact 110!")
        else:
            input("Please input any key to continue.\n")


