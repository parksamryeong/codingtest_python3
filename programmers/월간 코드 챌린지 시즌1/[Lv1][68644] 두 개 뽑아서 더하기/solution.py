def solution(numbers):
    answer = []
    
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            sum = numbers[i] + numbers[j]
            answer.append(sum)
    
    result = sorted(list(set(answer)))
    
    return result