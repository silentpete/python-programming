def make_car(manufacturer, model_name, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['manufacturer'] = manufacturer
    user_info['model_name'] = model_name
    return user_info

car = make_car("subaru", "outback", color="blue", location='colorado springs', tow_package='True')
print(car)
