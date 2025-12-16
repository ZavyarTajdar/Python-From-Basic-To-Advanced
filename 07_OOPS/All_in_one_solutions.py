# ************************************Solution: 1*******************************
class Car:
    total_car = 0

    def __init__(self, userbrand, usermodel):
        self.__brand = userbrand  # Kinda Private
        self.__model = usermodel # read-Only
        Car.total_car += 1
    
    def get_brand(self): # Getter
        return self.__brand+ " !"
    
    def set_brand(self, new_brand): # Setter
        self.__brand = new_brand

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self): # Polymorphism
        return "Petrol Or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"

    @property # Read-only decorator
    def model(self):
        return self.__model


# my_car = Car("Toyota", "Corolla")
# print(my_car.brand, my_car.model)
# print(my_car.full_name())
# 
# my_new_car = Car("Kia", "Sportage")
# print(my_new_car.brand, my_new_car.model)

# Inheritance
class Electri_Car(Car):
    def __init__(self, userbrand, usermodel, battery_size):
        super().__init__(userbrand, usermodel)
        self.battery_size = battery_size
    def fuel_type(self): # Polymorphism
        return "Electric Charge"

my_eCar = Electri_Car("Tesla", "S", "85kWh")

# print(isinstance(my_eCar, Car))
# print(isinstance(my_eCar, Electri_Car))

# print(my_eCar.get_brand())
# 
# safari = Car("Tata", "Safari")
# print(safari.fuel_type())
# print(Car.total_car)

# print(Car.general_description())


class Battery: 
    def batteryInfo(self):
        return "High Power Batter"

class Engine:
    def EngineInfo(self):
        return "High Power Engine"
    

class E_Car(Battery, Engine, Car):
    pass

new_carr = E_Car("Kia", "Carnival")
print(new_carr.EngineInfo())
print(new_carr.batteryInfo())