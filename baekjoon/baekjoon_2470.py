n = 6#int(input())
m = [18, 92, -47, 35, -84, -17]#list(map(int, input().split()))

left, right = 0, n - 1
min_mix = 100000000
solution = [0, 0]

m.sort()
print("Sort :", m)
while left < right:
    mix = m[left] + m[right]
    if abs(mix) < abs(min_mix):
        min_mix = mix
        solution = [left, right]
    if m[left + 1] < 0:
        left += 1
    else:
        right -= 1

answer = [m[solution[0]], m[solution[1]]]
answer.sort()
print(answer[0], answer[1])