from collections import deque
def solution(k, dungeons):
    answer = 0
    queue = deque()
    queue.append([k,[]])
    while queue:
        beh, visi = queue.popleft()
        for i in range(len(dungeons)):
            [a, b] = dungeons[i]
            if i not in visi and beh >= a and beh - b >= 0:
                queue.append([beh - b, visi + [i]])
            else:
                answer = max(answer, len(visi))
    return answer