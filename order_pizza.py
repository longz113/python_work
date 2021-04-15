make_pizza=[]
print('若想退出，请输入"退出"\n')
while 1:
    materials=input("请输入披萨的配料：")
    if materials=='退出':
        break
    else:
        make_pizza.append(materials)
        print('已经添加'+materials+'\n')
print('你的披萨配料包括：'+str(make_pizza))
    

        
