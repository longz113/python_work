
print('if you want to quit, please input "quit"')
while 1:
    scores=input('Please input "quit" or "your scores": ')
    if scores=='quit':
        break
    else:
        score=float(scores)
        if score>100 or score<0:
            print('You iput a wrong score')
        if 100>=score>=90:
            print('You get A')
        if score<90 and score>=80:
            print('You get B')
        if score<80 and score>=60:
            print('You get C')
        if score<60 and score>=0:
            print('You get D')
    print('')
