from itertools import combinations

def solution(nums):
    answer = 0
    takes = len(nums) // 2
    
    for selection in combinations(nums, takes):
        kinds = len(set(selection))
        
        answer = max(answer, kinds)
    
    return answer