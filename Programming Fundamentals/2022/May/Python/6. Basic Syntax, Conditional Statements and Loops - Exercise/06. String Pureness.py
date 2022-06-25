for i in range(int(input())):
    s = input()
    if not ("," in s or "." in s or "_" in s):
        print(f"{s} is pure.")
    else:
        print(f"{s} is not pure!")
