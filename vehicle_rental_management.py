from abc import ABC,abstractmethod
class  Vehicle(ABC):
    def __init__(self,vehicle_name,rental_price,days):
        self.vehicle_name=vehicle_name
        self.__rental_price=rental_price
        self.days=days
    @property
    def rental_price(self): 
        return self.__rental_price  
    @abstractmethod
    def calculate_rent(self,days):
        pass
    
class Car(Vehicle):
    def display_vehicle_details(self,vehicle_name,rental_price,days):
        self.vehicle_name=vehicle_name
        self.__rental_price=rental_price
        self.days=days
            
        print(self.vehicle_name)
        print(self.rental_price)
        print(self.days)
    def calculate_rent(self, days):
        
        print("Rental price: ",(self.rental_price*days)+500)  
class Bike(Vehicle):
    def display_vehicle_details(self,vehicle_name,rental_price,days):
        self.vehicle_name=vehicle_name
        self.__rental_price=rental_price
        self.days=days
                
        print(self.vehicle_name)
        print(self.rental_price)
        print(self.days)
    def calculate_rent(self, days):
        print("Rental price: ",(self.rental_price*days)+100)  


car=Car("car",1000,3)
car.display_vehicle_details("car",1000,3)
car.calculate_rent(3)
bike=Bike("bike",2000,3)
bike.display_vehicle_details("bike",2000,3)
bike.calculate_rent(3)

#output
# car
# 1000
# 3
# Rental price:  3500
# bike
# 2000
# 3
# Rental price:  6100

