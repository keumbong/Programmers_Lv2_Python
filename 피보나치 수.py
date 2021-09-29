def solution(n):
    num1, num2 = 0, 1
    for i in range(n):
        num1, num2 = num2, num1+num2
    if n >= 2:
        num1 = num1%1234567
    return num1