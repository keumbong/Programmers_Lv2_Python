def solution(word):
    answer = 0
    word = list(word)
    word_dic = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    max_num = 5 ** 5

    for i in word:
        answer += word_dic[i] * (max_num - 1) // 4
        max_num //= 5
    answer += len(word)
    return answer