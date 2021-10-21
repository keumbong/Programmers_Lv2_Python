def solution(people, limit):
    cnt = 0
    first = 0
    last = len(people) - 1
    people.sort()
    while first <= last:
        if people[first] + people[last] > limit:
            cnt += 1
            last -= 1
        else:
            cnt += 1
            first += 1
            last -= 1
    return cnt