def solution(n, lost, reserve):
    answer = 0
    
    new_lost = set(lost) - set(reserve)
    new_reserve = set(reserve) - set(lost)
    
    for s in new_reserve:
        if s-1 in new_lost:
            new_lost.remove(s-1)
        elif s+1 in new_lost:
            new_lost.remove(s+1)
    
    answer = n - len(new_lost)
    
    return answer