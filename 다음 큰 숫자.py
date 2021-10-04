def solution(n):
    answer = 0
    x = n + 1
    n_cnt = str(bin(n)[2:]).count('1')

    while True:
        x_cnt = str(bin(x)[2:]).count('1')
        if n_cnt == x_cnt:
            answer = x
            break
        else:
            x += 1
    return answer