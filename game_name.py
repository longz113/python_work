current_names=['dema','huangzi','bulong','yasuo','jie','xiaoyu']
print('Please create a new game name!\n')
print('Input "quit" to game over at any time.\n')
a=1
while a:
    name=input('Please input "quit" or your name: ')
    new_name=name.strip()
    if  new_name=='quit':
        break
    else:
        for current_name in current_names:
            if new_name.lower()!=current_name.lower():
                a=0
            else:
                print('This name is not OK, please try again.\n')
                a=1
                break
if a==0:
    print('You name is OK')
    current_names.append(new_name)
    print(current_names)



        
