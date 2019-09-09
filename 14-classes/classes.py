from dog import Dog
from car import Car
from electric_car import ElectricCar, Battery

# other ways to import classes
# import single class - 
#   from car import Car
# multiple classes in a single file - 
#   from car import ElectricCar
# importing multiple classes from a single module - 
#   from car import Car, ElectricCar
# import an entire module - 
#   import car
# import all classes from a module - 
#   from car import *
# import a module into a module - 
#   from ElectricCar from battery import Battery
# using aliases - 
#   from electic_car import ElectricCar as EC
#   use: my_tesla = EC('tesla', 'roadster', 2019)



# Classes should be camelcase
# instances should use '_'

my_dog = Dog('fido', 6)

# dot notation to access class attribute
print(f"\nMy dog's name is {my_dog.name.title()}")
print(f"my dog's age is {my_dog.age}")

my_dog.sit()
my_dog.roll_over()

your_dog = Dog('lucy', 3)
print(f"\nYour dog's name is {your_dog.name.title()}")
print(f"Your dog's age is {your_dog.age}")
your_dog.sit()
your_dog.roll_over()

# car class
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_description())
print(f"And it has {my_new_car.read_odometer()} miles on it.")

# set values
my_new_car.odometer_reading = 23
print(f"odometer reading for {my_new_car.get_description()} is {my_new_car.read_odometer()}")
my_new_car.read_odometer()

my_new_car.update_odometer(54)
print(f"odometer reading for {my_new_car.get_description()} is {my_new_car.read_odometer()}")

my_new_car.increment_odometer(20)
print(f"odometer reading for {my_new_car.get_description()} is {my_new_car.read_odometer()}")

# make sure I can read multiple classes from a single module
my_battery = Battery()
print(f"my batter = {my_battery}")

# inheritance
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(f"odometer reading for {my_tesla.get_description()} is {my_tesla.read_odometer()}")
print(f"{my_tesla.battery.describe_battery()}")
my_tesla.battery.get_range()

my_new_car.fill_gas_tank()
my_tesla.fill_gas_tank()