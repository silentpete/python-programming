from car import Car

my_new_car = Car("audi", "rs4", 2023)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 42
my_new_car.read_odometer()
