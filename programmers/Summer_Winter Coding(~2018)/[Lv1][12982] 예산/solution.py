def solution(d, budget):
    answer = 0
    sum = 0
    d.sort()
    
    for cost in d:
        if cost + sum <= budget:
            sum += cost
            answer += 1
        else:
            break
    
    return answer