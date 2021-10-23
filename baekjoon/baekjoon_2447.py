import math

N = int(input())
pattern = [
    "***",
    "* *",
    "***"
]
blank = [
    "   ",
    "   ",
    "   "
]

def is_blank(w, h):
    for i in range(int(math.log(N, 3))):
        if ((w // (3 ** i)) % 3 == 1 and (h // 3 // (3 ** i)) % 3 == 1):
            return True
    return False

for h in range(N):
    for w in range(N // 3):
        if is_blank(w, h):
            print(blank[h%3], end="")
        else:
            print(pattern[h%3], end="")
    print()

