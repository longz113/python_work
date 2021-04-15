class User():
    def __init__(self,first_name,last_name,*information):
        self.first_name=first_name
        self.last_name=last_name
        self.information=information
        self.name=self.first_name+self.last_name
    def describe(self):
        if self.information:
            inf=''
            for information in self.information:
                inf=inf+' '+str(information)
            print(name+' '+inf)
        else:
            print(name)
        
    def greet(self):
        print('Hello! '+self.name)

# ------------------------------------------------------
class Car():
    def __init__(self,pinpai,xinghao,year):
        self.pinpai=pinpai
        self.xinghao=xinghao
        self.year=year
        self.meter=0
    def describe(self):
        long_name=str(self.year)+' '+self.pinpai+' '+self.xinghao
        return(long_name)
    def update_meter(self,increment):
        if increment>0:
           self.meter+=increment
    def read_meter(self):
        print('The meter is: '+str(self.meter))

a=Car('audi','a4','2016')
a.update_meter(10)
a.read_meter()
