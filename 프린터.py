from collections import deque
def solution(priorities, location):
    answer = 0
    queue = deque([(prior,num) for num,prior in enumerate(priorities)])
    while len(queue):
        q = queue.popleft()
        if queue and max(queue)[0] > q[0]:
            queue.append(q)
        else:
            answer += 1
            if q[1] == location:
                break
    return answer