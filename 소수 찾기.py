from itertools import permutations
import math

# 소수 판별 알고리즘
def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    arr = []
    cnt = 0
    # 순열을 이용해 숫자들의 경우의 수 찾기
    for i in range(1, len(numbers) + 1):
        arr += list(permutations(numbers, i))

    # 인자들을 join 및 int 화 시킴
    for i in range(len(arr)):
        arr[i] = int(''.join(arr[i]))

    # 순열에서 나온 중복된 숫자들 제거
    arr_ref = list(set(arr))
    arr_ref.sort()

    # 소수 판별
    for num in arr_ref:
        if is_prime(num):
            cnt += 1

    return cnt