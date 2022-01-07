def convert(arr):
    s = ""
    count = 1
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            count += 1
        else:
            if count > 1:
                s += str(count) + arr[i]
            else:
                s += arr[i]
            count = 1
    if count > 1:
        s += str(count) + arr[-1]
    else:
        s += arr[-1]
    return s

def solution(s):
    length = len(s)
    arr = []
    for n in range(1, length + 1):
        temp = []
        split = length // n
        for i in range(split):
            temp.append(s[n*i:n*(i+1)])
        if split * n != length:
            temp.append(s[split*n:])
        arr.append(len(convert(temp)))
    return min(arr)
