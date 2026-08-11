def solution(board, moves):
    
    basket = []
    
    result = 0
    
    for i in range(len(moves)):
        
        position = moves[i]-1
        
        for j in range(len(board)):
            if board[j][position] > 0:
                
                if len(basket) > 0 and basket[-1] == board[j][position]:
                    basket.pop()
                    result += 2
                else:
                    basket.append(board[j][position])
                
                board[j][position] = 0
                
                break
    
    return result