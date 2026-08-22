def solution(nums):
    answer = 0
    takes = len(nums) // 2
    
    types = len(set(nums))
    
    answer = min(takes, types)
    
    return answer