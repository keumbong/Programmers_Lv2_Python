import math

def solution(arr):
    answer = 1
    for i in range(len(arr)):
        gcd = math.gcd(answer, arr[i])
        answer = (answer * arr[i]) // gcd
    return answer