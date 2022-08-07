s = input()

cmd = input()

def translate(s: str, char: str, replacement: str) -> str:
    return s.replace(char, replacement)

def includes(s: str, substring: str) -> bool:
    return substring in s

def start(s: str, substring: str) -> bool:
    return s.startswith(substring)

def lowercase(s: str) -> str:
    return s.lower()

def find_index(s: str, substring: str) -> int:
    return s.rfind(substring)

def remove(s: str, start: int, count: int) -> str:
    return s[:start] + s[start+count:]

while cmd != 'End':
    cmd, *args = cmd.split()
    if cmd == 'Translate':
        s = translate(s, *args)
        print(s)
    elif cmd == 'Includes':
        print(includes(s, *args))
    elif cmd == 'Start':
        print(start(s, *args))
    elif cmd == 'Lowercase':
        s = lowercase(s)
        print(s)
    elif cmd == 'FindIndex':
        print(find_index(s, *args))
    elif cmd == 'Remove':
        args = [int(x) for x in args]
        s = remove(s, *args)
        print(s)
    cmd = input()

# Example input:
"""
//Thi5 I5 MY 5trING!//
Translate 5 s
Includes string
Start //This
Lowercase
FindIndex i
Remove 0 10
End

"""
# Example output:
"""
*S0ftUni is the B3St Plac3**
Translate 2 o
Includes best
Start the
Lowercase
FindIndex p
Remove 2 7
End

"""