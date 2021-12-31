def solution(s):
    arr = list(map(lambda x: list(map(lambda y: int(y), x.split(','))), s.replace('},', '|').replace('{', '').replace('}', '').split('|')))
    arr.sort(key=len)
    res = arr[0]
    for i in range(1, len(arr)):
        for v in res:
            if v in arr[i]: arr[i].remove(v)
        res.extend(arr[i])
    return res