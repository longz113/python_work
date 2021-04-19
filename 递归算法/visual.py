
from turtle import Turtle
import random
'''
#小乌龟旋转图
myTurtle=Turtle()
myWin=myTurtle.getscreen()

def drawspiral(myTurtle,linelen):
    if linelen>0:
        myTurtle.forward(linelen)
        myTurtle.right(90)
        drawspiral(myTurtle,linelen-5)

drawspiral(myTurtle,100)
myWin.exitonclick()
'''
'''
#分形树
mytree=Turtle()
mytree.left(90)
mytreewin=mytree.getscreen()
def drawtrees(mytree,treelen):
    if treelen>0:
        mytree.forward(treelen)
        mytree.right(15)
        drawtrees(mytree,treelen-random.randrange(10,30))
        mytree.left(30)
        drawtrees(mytree,treelen-random.randrange(15,30))
        mytree.right(15)
        mytree.backward(treelen)        
drawtrees(mytree,100)
mytreewin.exitonclick()

'''

#谢尔平斯基三角形
spstr=Turtle()
spstrwin=spstr.getscreen()
def drawspstr(spstr,sidelen):
    if sidelen>1:
        spstr.left(60)
        spstr.forward(sidelen)
        spstr.left(120)
        spstr.forward(sidelen)
        spstr.left(120)
        spstr.forward(sidelen)
        spstr.left(120)
        spstr.forward(sidelen/2)
        drawspstr(spstr,sidelen/2)

drawspstr(spstr,200)
spstrwin.exitonclick()
        































