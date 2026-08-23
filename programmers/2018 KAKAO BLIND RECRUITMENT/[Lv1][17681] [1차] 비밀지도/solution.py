def solution(n, arr1, arr2):
    answer = []
    
    for row1, row2 in zip(arr1, arr2):
        bit = bin(row1 | row2)[2:].zfill(n)
        
        row = bit.replace('1', '#').replace('0', ' ')
        answer.append(row)
    
    return answer