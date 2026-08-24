def solution(N, stages):
    fail_rates = []
    challengers = len(stages)
    
    for stage in range(1, N + 1):
        
        not_finished = stages.count(stage)
        
        if challengers == 0:
            fail_rate = 0.0
        else:
            fail_rate = not_finished / challengers
            
        fail_rates.append((stage, fail_rate))
        
        challengers -= not_finished

    fail_rates.sort(key=lambda x: (-x[1], x[0]))
    
    answer = [stage for stage, rate in fail_rates]
        
    
    return answer