from turtle import color


def make_car(make,model, **car_info):
    """Build a dictionary containing everything we know about a user"""
    car_info['car make'] = make
    car_info['car model'] = model
    return car_info

car_profile = make_car('VW', 'Jetta', color='black', tow_package =True)

print(car_profile)