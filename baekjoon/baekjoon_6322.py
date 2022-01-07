i = 0
while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    if i > 0:
        print()
    print(f"Triangle #{i+1}")
    if c == -1:
        x = (a ** 2 + b ** 2) ** 0.5
        print("c = {:.3f}".format(x))
    elif max(a, b) >= c:
        print("Impossible.")
    elif a == -1:
        x = (c ** 2 - b ** 2) ** 0.5
        print("a = {:.3f}".format(x))
    else:
        x = (c ** 2 - a ** 2) ** 0.5
        print("b = {:.3f}".format(x))
    i += 1