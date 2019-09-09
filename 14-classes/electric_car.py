from car import Car
# from battery import Battery

class Battery :
    """ A simple class for an electric car battery"""

    def __init__(self, battery_size=75) :
        """Initialize battery attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print battery attributes"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print statement about the range the battery provides"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car) :
    def __init__(self, make, model, year) :
        """Represents aspects of a car specific to electric vehicles"""
        super().__init__(make, model, year)
        self.battery = Battery()

#    def describe_battery(self) :
#       """print out the battery size"""
#        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self) :
        """electric cars don't have gas tanks"""
        print("This car doesn't need gas!")