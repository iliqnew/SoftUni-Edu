s1 = input()
s2 = input()

for i in range(len(s1)):
    if s1[i] != s2[i]:
        s1 = s1[:i] + s2[i] + s1[i+1:]
        print(s1)