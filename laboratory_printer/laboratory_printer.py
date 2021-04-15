'''
引入模板
每秒可能进行的工作
    创建打印任务

    是否有打印任务，打印机是否正在工作
       开始打印
       计算等待了多久
       计算本次任务需要打印多长时间
    打印时间倒计时   

'''
from queue import Queue
from printer import Printer
from task import Task
import random

def creat_newtask():
    if random.randrange(1,181)==180:
        return True
    else:
        return False


waittime=[]
tasklist=Queue()
lab_printer=Printer(12)
average_waittime=0

for current_second in range(3600):
    if creat_newtask():
        newtask=Task(current_second)
        tasklist.put(newtask)
    if  not tasklist.empty() and not lab_printer.busy():
        currenttask=tasklist.get()
        
        i=current_second-currenttask.creat_second
        waittime.append(i)
        
        lab_printer.start_newtask(currenttask)
        
    lab_printer.remain_time()
if len(waittime)!=0:
    average_waittime=sum(waittime)/len(waittime)
print('average_waittime of %d task is %.4f.'%(len(waittime),average_waittime))









