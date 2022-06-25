budget = float(input())

eggs_needed = 1
flour_needed = 1
milk_needed = 0.25

flour_price = float(input())
eggs_price = flour_price * .75
milk_price = flour_price * 1.25

loaves = 0
eggs = 0

flour = 1
eggs = 1
milk = 1

while True:
    if flour < flour_needed:
        if budget >= flour_price:
            budget -= flour_price
            flour += 1
        else:
            break
    if eggs < eggs_needed:
        if budget >= eggs_price:
            budget -= eggs_price
            eggs += 1
        else:
            break
    if milk < milk_needed:
        if budget >= milk_price:
            budget -= milk_price
            milk += 1
        else:
            break
    
    flour -= flour_needed
    eggs -= eggs_needed
    milk -= milk_needed
    
    loaves += 1
    eggs += 3
    if loaves % 3:
        eggs -= loaves - 2
    
print(f"You made {loaves} loaves of Easter bread! Now you have {eggs} eggs and {budget:.2f}BGN left.")
