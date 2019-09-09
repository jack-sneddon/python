class Car :
    def __init__(self, make, model, year) :
        self.make = make
        self.model = model
        self.year = year
        # default to a new car
        self.odometer_reading = 0

    def get_description(self) :
        """Return a neatly formed description of the car."""
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()

    def read_odometer(self) :
        """ what is the odemeter reading"""
        return self.odometer_reading

    def update_odometer(self, mileage) :
        """ update the odometer reading"""
        if(mileage >= self.odometer_reading) :
            self.odometer_reading = mileage
        else :
            print("You can't roll back the odometer!")

    def increment_odometer (self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self) :
        print(f"{self.get_description()} filling up with gas.")