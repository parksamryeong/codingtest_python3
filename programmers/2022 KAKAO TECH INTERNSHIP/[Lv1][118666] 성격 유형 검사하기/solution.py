def solution(survey, choices):
    
    scores = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 
              'J': 0, 'M': 0, 'A': 0, 'N': 0}
    
    for s, c in zip(survey, choices):
        disagree = s[0]
        agree = s[1]
        
        if c < 4:

            scores[disagree] += (4 - c)
        elif c > 4:
            scores[agree] += (c - 4)

            
    indicators = ["RT", "CF", "JM", "AN"]
    answer = ''
    
    for ind in indicators:
        type1 = ind[0]
        type2 = ind[1]
        
        if scores[type1] >= scores[type2]:
            answer += type1
        else:
            answer += type2
            
    return answer