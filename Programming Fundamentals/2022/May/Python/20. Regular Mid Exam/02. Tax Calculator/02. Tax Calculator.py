cars_info = input()
cars_info_list = cars_info.split('>>')

taxes_total = 0

for car_info in cars_info_list:
    car_info = car_info.split(' ')
    
    car_type = car_info[0]
    years = int(car_info[1])
    mileage = int(car_info[2])
    
    if car_type == "family":
        tax = 50
        tax -= years * 5
        tax += mileage // 3000 * 12
    elif car_type == "heavyDuty":
        tax = 80
        tax -= years * 8
        tax += mileage // 9000 * 14
    elif car_type == "sports":
        tax = 100
        tax -= years * 9
        tax += mileage // 2000 * 18
    else:
        print(f"Invalid car type.")
        continue
    print(f"A {car_type} car will pay {tax:.2f} euros in taxes.")
    taxes_total += tax

print(f"The National Revenue Agency will collect {taxes_total:.2f} euros in taxes.")
