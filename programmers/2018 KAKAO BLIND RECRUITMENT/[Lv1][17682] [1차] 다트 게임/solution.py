def solution(dartResult):
    answer = 0
    scores = []
    i = 0
    
    while i < len(dartResult):
        if dartResult[i:i+2] == '10':
            score = 10
            i += 2
        else:
            score = int(dartResult[i])
            i += 1
            
        bonus = dartResult[i]
        if bonus == 'S':
            score **= 1
        elif bonus == 'D':
            score **= 2
        elif bonus == 'T':
            score **= 3
        i += 1
        
        if i < len(dartResult) and dartResult[i] in ('*', '#'):
            option = dartResult[i]
            if option == '*':
                score *= 2
                if len(scores) > 0:
                    scores[-1] *= 2
            elif option == '#':
                score *= -1
            i += 1
            
        scores.append(score)
    
    answer = sum(scores)
    
    return answer