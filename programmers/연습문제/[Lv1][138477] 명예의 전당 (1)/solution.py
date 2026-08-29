def solution(k, score):
    answer = []
    rank = []
    
    for s in score:
        rank.append(s)
        if len(rank) < k:
            answer.append(min(rank))
        else:
            top_k = sorted(rank, reverse=True)[:k]
            answer.append(min(top_k))
    
    return answer