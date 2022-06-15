def is_kid(age):
    if age > 14:
        return False
    return True

def is_teen(age):
    if 14 < age <= 18:
        return True
    return False

def is_young_adult(age):
    if 18 < age <= 21:
        return True
    return False

def is_adult(age):
    if age > 21:
        return True
    return False

age = int(input())

if is_kid(age):
    print("Drink toddy")
elif is_teen(age):
    print("Drink coke")
elif is_young_adult(age):
    print("Drink beer")
elif is_adult(age):
    print("Drink whisky")

