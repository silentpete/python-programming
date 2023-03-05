class Restaurant:
    """A simple restaurant example"""

    def __init__(self, restaurant_name, restaurant_cuisine_type) -> None:
        """instance of Restaurant defaults"""
        self.restaurant_name = restaurant_name
        self.restaurant_cuisine_type = restaurant_cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """output the details of this restaurant"""
        print(f"{self.restaurant_name} restaurant serves {self.restaurant_cuisine_type} food.")

    def open_restaurant(self):
        """output that the restaurant is open"""
        print("the restaurant is now open")

    def customers_served(self):
        """Print number of customers served."""
        print(f"{self.restaurant_name} has served {self.number_served} customers.")

    def set_number_served(self, served):
        """Set the number of customers served"""
        self.number_served = served

    def increment_number_served(self, increment):
        """Increment the number served."""
        self.number_served += increment

class IceCreamStand(Restaurant):
    """An Ice Cream Stand type of Restaurant"""

    def __init__(self, restaurant_name, restaurant_cuisine_type):
        super().__init__(restaurant_name, restaurant_cuisine_type)
        self.flavors = ["chocolate", "mint chocolate", "vanilla", "chocolate peanutbutter"]

    def available_flavors(self):
        """print available flavors"""
        print(f"{self.restaurant_name} has the following flavors:")
        for flavor in self.flavors:
            print(f"{flavor}")

some_restaurant = Restaurant("Harvy's", "Greek")
some_restaurant.describe_restaurant()
some_restaurant.open_restaurant()
some_restaurant.set_number_served(23)
some_restaurant.increment_number_served(64)
some_restaurant.customers_served()

another_restaurant = IceCreamStand("Nicole's", "Ice Cream")
another_restaurant.available_flavors()
