def solution(name):
    answer, n = 0, 0
    move = len(name) - 1
    for i, char in enumerate(name):
        answer += min(ord(char)-ord('A'), ord('Z')-ord(char) + 1)
        n = i + 1
        while n < len(name) and name[n] == 'A':
            n += 1
        move = min(move, i + i + len(name) - n)
    answer += move
    return answer