def solution(enter, leave):
    n = 0
    cnt = [0 for _ in range(len(enter))]
    for l in leave:
        idx = enter.index(l)
        if (n < idx): n = idx
        enter.remove(l)
        cnt[l - 1] += n
        for i in range(n):
            cnt[enter[i] - 1] += 1
        n -= 1
    return cnt