#import Task

class Printer():
    def __init__(self,ppm):
        self.ppm=ppm
        self.print_task=None
        self.remaintime=0
        
    def busy(self):
        if self.print_task==None:
            return False
        else:
            return True
        
    def start_newtask(self,currenttask):
        self.print_task=currenttask
        self.print_pages=self.print_task.getpages()
        self.remaintime=self.print_pages*self.ppm

    def remain_time(self):
        if self.remaintime>0:
            self.remaintime=self.remaintime-1
        else:
            self.remaintime=0
            self.print_task=None
        



