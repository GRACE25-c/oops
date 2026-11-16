from abc import ABC,abstractmethod
class  Employee(ABC):
    def __init__(self, basic_salary,name,work_mode):
        self. __basic_salary=basic_salary
        self.name=name
        self.work_mode=work_mode
        
    @property
    def basic_salary(self):
        return   self.__basic_salary
    @abstractmethod
    def calculate_salary(self):
        pass
    
class  PermanentEmployee(Employee):
    def  display_details(self, basic_salary,name,work_mode):
        
        print("name: ",name)
        print("work mode: ",work_mode)
        print("basic salary: ",basic_salary)
        
     
    def calculate_salary(self,basic_salary,allowance):
        self.allowance=allowance
        self.__basic_salary=basic_salary
        
    
        print( "Permanent Employee: ",self.basic_salary + (0.2*self.allowance) ) 
        
class ContractEmployee(Employee):
    def  display_details(self, basic_salary,name,work_mode):
        
        print("name: ",name)
        print("work mode: ",work_mode)
        print("basic salary: ",basic_salary)
    def calculate_salary(self,basic_salary,allowance):
        self.allowance=allowance
        self.__basic_salary=basic_salary
        
        print("Contract Employee: ",self.basic_salary + (0.05*self.allowance))   #5/100*basic salary

permenentemployee=PermanentEmployee(100000,"Grace","permenent employee")
permenentemployee.display_details(100000,"Grace","permenent employee")
permenentemployee.calculate_salary(10000,50000)
contractemployee=ContractEmployee(90000,"Jacob","contract employee")
contractemployee.display_details(90000,"Jacob","contract employee")
contractemployee.calculate_salary(90000,40000)

# #output
# name:  Grace
# work mode:  permenent employee
# basic salary:  100000
# Permanent Employee:  110000.0
# name:  Jacob
# work mode:  contract employee
# basic salary:  90000
# Contract Employee:  92000.0



