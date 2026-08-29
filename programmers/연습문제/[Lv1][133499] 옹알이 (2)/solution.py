def solution(babbling):
    words = ["aya", "ye", "woo", "ma"]
    answer = 0
    
    for b in babbling:
        if any(w + w in b for w in words):
            continue
        
        comb = b
        for w in words:
            comb = comb.replace(w, " ")
        
        if comb.strip() == "":
            answer += 1
            
    return answer