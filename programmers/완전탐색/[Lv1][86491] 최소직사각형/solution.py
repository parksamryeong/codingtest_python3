def solution(sizes):
    answer = 0
    max_w = 0
    max_h = 0

    for i in range(len(sizes)):
        w = sizes[i][0]
        h = sizes[i][1]
        if w < h:
            w, h = h, w
        
        if w > max_w:
            max_w = w
        
        if h > max_h:
            max_h = h

    answer = max_w * max_h

    return answer