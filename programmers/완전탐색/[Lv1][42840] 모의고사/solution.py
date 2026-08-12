def score(pattern, answers):
    score = 0
    
    for i in range(len(answers)):
        if answers[i] == pattern[i % len(pattern)]:
            score += 1
    
    return score

def solution(answers):
    scores = []    
    top_student = []
    
    pattern1 = [1,2,3,4,5]    
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    
    student1 = score(pattern1, answers)
    student2 = score(pattern2, answers)
    student3 = score(pattern3, answers)
    
    scores.append(student1)
    scores.append(student2)
    scores.append(student3)
    
    max_score = max(scores)
    
    for k in range(3):
        if scores[k] == max_score:
            top_student.append(k+1)
        
    return top_student