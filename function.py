def print_name(name):
    print(f"my name is {name}")

print_name("samudu")

def add_two(num):
    return num +2
result =  add_two(2)


# parameters vs arguments

def contact_card(name,age,car_model):
    return f"{name} is {age} and drives a {car_model}"

def can_drive(age, driving_age =16):
    return age >= driving_age



