coffees = 0
while True:
    s = input()
    if s == "END":
        break
    elif s in ["coding", "dog", "cat", "movie"]:
        coffees += 1
    elif s in ["CODING", "DOG", "CAT", "MOVIE"]:
        coffees += 2

if coffees > 5:
    print("You need extra sleep")
else:
    print(coffees)