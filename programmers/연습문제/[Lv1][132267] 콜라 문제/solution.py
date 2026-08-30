def solution(a, b, n):
    answer = 0
    
    while n >= a:
        coke = (n // a) * b
        answer += (n // a) * b
        n = (n % a) + coke
        
    return answer