
width, height = [int(i) for i in input().split()]
x, y, d = [int(i) for i in input().split()]

maps = []
for j in range(height):
    maps.append([int(i) for i in input().split()])

print()

# 8, 6, 2, 4
direction = ['^', '>', 'v', '<']

def setDir(d):
    s = d
    d = []
    for i in range(4):
        d.append(s)
        s += 1
        if s > 3:
            s = 0
    return d

d = setDir(d)


def isPassable(stack, x, y, d):
    if d == 1:
        x += 1
    elif d == 3:
        x -= 1
    if d == 0:
        y -= 1
    elif d == 2:
        y += 1

    if maps[y][x] == 0 and not (x, y) in stack:
        return True, x, y
    else:
        return False, x, y

def display(x, y, d):
    for h in range(len(maps)):
        for w in range(len(maps[h])):
            if x == w and y == h:
                print(f"{direction[d]} ", end="")
            else:
                print(f"{maps[h][w]} ", end="")
        print()

def move(x, y, d, stack, cnt = 1):
    stack.append((x, y))
    old_cnt = cnt
    for p in d:
        check, new_x, new_y = isPassable(stack, x, y, p)
        if check:
            display(new_x, new_y, p)
            print()
            new_d = setDir(p)
            cnt = move(new_x, new_y, new_d, stack, cnt + 1)
    return cnt

cnt = move(x, y, d, [])
print(cnt)
            

