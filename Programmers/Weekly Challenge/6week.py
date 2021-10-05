def solution(weights, head2head):
    l = len(weights)
    boxers = []
    for i, w in enumerate(weights):
        win = 0
        lose = 0
        w2b = 0
        rate = 0
        for idx, r in enumerate(list(head2head[i])):
            if r == 'W':
                win += 1
                if (w < weights[idx]):
                    w2b += 1
            elif r == 'L':
                lose += 1
        if (win + lose > 0):
            rate = win / (win + lose)
            
        boxers.append([rate, w2b, w, -(i+1)])
        
    boxers.sort(reverse=True)
    answer = []
    for i in range(l):
        answer.append(-boxers[i][3])
    
    return answer