class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas_tank_percent = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if someone trys to role back the mileage.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back an odometer.")

    def increment_odometer(self, mileage):
        """add the given amount to the odometer reading"""
        self.odometer_reading += mileage

    def fill_gas_tank(self, percent):
        """set gas tank percent"""
        if percent >100:
            print("you over filled the gas task, set to 100 percent.")
            self.gas_tank_percent = 100
        elif percent <1:
            print(f"you didn't put any gas in the tank, still at {self.gas_tank_percent}.")
        else:
            self.gas_tank_percent = percent

class Battery:
    """A simple attemp to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        """Upgrade the battery if it is less than 100"""
        if self.battery_size < 100:
            self.battery_size = 100

class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""

    def __init__(self, make, modle, year):
        """
        Initialize attributes of parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, modle, year)
        self.battery = Battery()
        self.gas_tank_percent = "N/A"

    def fill_gas_tank(self, percent):
        """Electric cars don't hae gas tanks."""
        print("No gas tank.")

car_a = Car("Ford", "Pinto", "1970")
print(car_a.get_descriptive_name())

car_a.update_odometer(196_784)
car_a.read_odometer()

car_a.increment_odometer(456)
car_a.read_odometer()

car_b = ElectricCar("tesla", 'modle s', 2019)
print(car_b.get_descriptive_name())
car_b.battery.describe_battery()
car_b.battery.get_range()
car_b.fill_gas_tank(8)
print(car_b.gas_tank_percent)

car_c = ElectricCar("gmc", "volt", 2020)
car_c.battery.get_range()
car_c.battery.upgrade_battery()
car_c.battery.get_range()
