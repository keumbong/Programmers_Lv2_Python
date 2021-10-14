def solution(s):
    z_cnt, s_len, cnt = 0, 0, 0
    remove_set = {'0'}

    while True:
        z_cnt += s.count('0')
        s = [i for i in s if i not in remove_set]
        s_len = len(s)
        s = bin(s_len)[2:]
        cnt += 1
        if s == '1':
            break

    return [cnt, z_cnt]