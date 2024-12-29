#define class char.--->var actions--->method
#instance var id--->depend obj
#class var count-->shred with objects
class Human:
    #class var
    count=0
    def __init__(self,id,name):
        #instance var
        self.id=id
        self.name=name
        Human.count+=1
    def speak(self):
        print(f'iam {self.name}')
    def __str__(self):
        return  self.name+' '+str(self.id)

class Employee(Human):
    def __init__(self,id,name,salary):
        super(Employee,self).__init__(id,name)
        self.__salary=salary#private accsess inside class
    # def setsalary(self,newsalary):
    #     if(newsalary>=3000 and newsalary<=8000):
    #         self.__salary=newsalary
    #     else:
    #         print('invalid salary')
    # def getsalary(self):
    #     return self.__salary
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self,new):
        if(new>=3000 and new<=8000):
            self.__salary=new
        else:print('invalid salary')
    # #overriding
    def speak(self):
        # super(Employee,self).speak()
        print(f'my salary ={self.__salary}')
    def __str__(self):
        # return f'{self.id} {self.name} {self.salary}'
        return super(Employee,self).__str__()+'  '+str(self.__salary);

#obj
ali=Human(1,'ali')#call const
# print(Human.count)
aya=Human(2,'aya')
# print(Human.count)
mark=Human(3,'mark')
#obj employee
e1=Employee(12,'sara',5000)
e1.salary=7000
print(e1.salary)
print(ali)
print(e1)
# e1.setsalary(7000)
# print(e1.getsalary())
# print(e1.__salary)
# e1.setsalary(40000000000)
# print(e1.getsalary())
# # ali.speak()
# e1.speak()
# print(e1.salary)
# e1.salary=90
#accsess instance var
# print(ali.id,aya.id,mark.id)
#accsess class var
# print(Human.count,ali.count)



# from myexperiance.cloud.awsmod import createec2
# createec2()
# from myexperiance import simplefileopertion
# simplefileopertion.read()
# import myexperiance.simplefileopertion as r
# r.read('asd.txt',5)
# from myexperiance import simplefileopertion as sim
#
# print(sim.read('asd.txt','all'))
# from myexperiance.simplefileopertion import read as r
# print(r('asd.txt',5))

# print(read('asd.txt',5))
# print(read('asd.txt','all'))
# print('====',read('asd.txt','line'))
# print('====',read('asd.txt','lines'))
# print('====',read('asd.txt','li'))

# writetofile('asd.txt','hi cloud arch')
# writetofile('asd2.txt','hi cloud arch smart')
# writetofile('asd2.txt','hi cloud arch alex')
#standred
# email=input('enter email')
# reg1 =  r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
# print(re.match(reg1,email))
# print(re.fullmatch(reg1,email))
# print(re.search(reg1,email))
# print(re.findall(reg1,email))

# userpassword=input('enter password')
# reg = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
# print(re.findall(reg,userpassword))
#
# if(re.fullmatch(reg,userpassword) is not None):
#     print('password is ok')
# else:
#     print('password not valid')


# print(sys.getprofile())
# print('ls -l / 2> err.txt >> out.txt ')

# print(sys.exc_info()[1])
# print(sys.argv)

# print(os.name)
# if(os.name=='posix'):
#     print('run mv')
# else:
#     print('run mv command win')
# if(os.getlogin()=='root'):
#     print('iam root')
# else:
#     print('other user')



# # os.chmod('asd.txt',)
#
# os.chdir('/')
# print(os.system('ls'))
# # # print(os.path.exists('/'))
# # if(os.path.exists('/etc/passwod')):
# #     print('ok')
# # else:
# #     print('not found')
