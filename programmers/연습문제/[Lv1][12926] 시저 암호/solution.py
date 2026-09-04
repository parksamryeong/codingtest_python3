def solution(s, n):
    answer = ''
    
    for char in s:
        if char.isupper():
            sol = chr((ord(char) - ord('A') + n) % 26 + ord('A'))
            answer += sol
            
        elif char.islower():
            sol = chr((ord(char) - ord('a') + n) % 26 + ord('a'))
            answer += sol
            
        else:
            answer += char
    
    return answer