import itertools
def solution(numbers):
    arr, st = [], ''
    answer = itertools.permutations(numbers, len(numbers))
    for i in answer:
        for j in i:
            st = st + str(j)
        arr.append(st)
        st = ''
    return max(arr)
# 이 방식은 시간 복잡도 문제가 있음 (permutations사용)

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x : x*3, reverse = True)
    return str(int(''.join(numbers)))