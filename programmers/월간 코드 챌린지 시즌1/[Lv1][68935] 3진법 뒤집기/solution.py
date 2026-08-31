def solution(n):
    num = ""
    
    while n > 0:
        num += str(n % 3)
        n = n // 3
    
    answer = int(num, 3)
    
    return answer