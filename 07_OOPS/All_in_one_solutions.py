# ************************************Solution: 1*******************************
class Car:
    total_car = 0

    def __init__(self, userbrand, usermodel):
        self.__brand = userbrand  # Kinda Private
        self.model = usermodel
        Car.total_car += 1
    
    def get_brand(self): # Getter
        return self.__brand+ " !"
    
    def set_brand(self, new_brand): # Setter
        self.__brand = new_brand

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self): # Polymorphism
        return "Petrol Or Diesel"

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
print(my_eCar.get_brand())

safari = Car("Tata", "Safari")
print(safari.fuel_type())
print(Car.total_car)