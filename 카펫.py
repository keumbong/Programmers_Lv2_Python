def solution(brown, yellow):
    total = brown + yellow
    answer = []
    for w in range(3, total):
        h = int(total // w)
        if (w >= h) and (w * h == total) and ((h-2)*(w-2) == yellow):
            answer = [w,h]
            break
    return answer