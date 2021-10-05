N = int(input())

if N <= 99:
    print(N)
else:
    forward = []
    for f in range(10):
        for d in range(5):
            if f + d * 2 < 10:
                forward.append([f, f+d, f+d*2])
            else:
                break
    backward = []
    for f in forward:
        backward.append(list(reversed(f)))
    HAN = set([])
    for f in forward:
        HAN = HAN.union(set([f[0]*100 + f[1]*10 + f[2]]))
    for b in backward:
        HAN = HAN.union(set([b[0]*100 + b[1]*10 + b[2]]))
    
    HAN = list(HAN)
    HAN.sort()
    del HAN[0:5]
    cnt = 0
    for i, h in enumerate(HAN):
        if (N >= h):
            cnt += 1
        else:
            break
    print(99 + cnt)