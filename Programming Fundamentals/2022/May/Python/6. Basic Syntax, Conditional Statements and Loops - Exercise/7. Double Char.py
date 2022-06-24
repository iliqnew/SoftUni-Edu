while True:
    s = input()
    if s == "End":
        break
    elif s == "SoftUni":
        pass
    else:
        new_s = ""
        for c in s:
            new_s += c * 2
        print(new_s)
