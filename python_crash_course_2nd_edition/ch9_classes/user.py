class User:
    """instance of User defaults"""

    def __init__(self, first_name, last_name, age) -> None:
        """instance of User defaults"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is {self.age} years old.")

    def greet_user(self):
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}!")

    def increment_login_attempts(self):
        """Increase login attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login attempts"""
        self.login_attempts = 0

class Admin(User):
    """A special kind of user"""

    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        """print the Admin privileges"""
        print(f"The Admin user {self.first_name} has the following privileges")
        for privilege in self.privileges:
            print(f"{privilege}")


user = User("peter", "gallerani", "42")

user.describe_user()
user.greet_user()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)

user = Admin("nicole", "gallerani", 37)
user.show_privileges()
