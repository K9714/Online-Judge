def solution(scores):
    answer = ''
    grade = ['A', 'B', 'C', 'D', 'F']
    
    for n in range(len(scores)):
        score = []
        for i in range(len(scores)):
            score.append(scores[i][n])
        eva = scores[n][n]
        if score.count(eva) == 1 and eva == max(score): score.remove(eva)
        if score.count(eva) == 1 and eva == min(score): score.remove(eva)
        if len(score) == 0:
            avg = 0
        else:
            avg = sum(score) / len(score)
        idx = 9 - int(avg / 10)
        if idx == 4: idx = 3
        idx = max(0, idx)
        idx = min(idx, len(grade) - 1)
        answer += grade[idx]
    
    return answer