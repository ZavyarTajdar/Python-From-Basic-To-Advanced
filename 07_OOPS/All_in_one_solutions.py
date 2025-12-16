# ************************************Solution: 1*******************************
class Car:
    def __init__(self, userbrand, usermodel):
        self.__brand = userbrand  # Kinda Private
        self.model = usermodel
    
    def get_brand(self):
        return self.__brand+ " !"

    def full_name(self):
        return f"{self.__brand} {self.model}"

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

my_eCar = Electri_Car("Tesla", "S", "85kWh")
print(my_eCar.get_brand())


