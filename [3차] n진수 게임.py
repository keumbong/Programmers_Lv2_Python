def solution(n, t, m, p):
    answer, answer_all = '', []

    def convert(num, jin):
        num_list = '0123456789ABCDEF'
        div, mod = divmod(num, jin)
        if div == 0:
            return num_list[mod]
        else:
            return convert(div, jin) + num_list[mod]

    for i in range(t * m):
        con = convert(i, n)
        for j in con:
            answer_all.append(j)

    for i in range(p - 1, t * m, m):
        answer = answer + answer_all[i]
    return answer