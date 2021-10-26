from collections import deque


def solution(bridge_length, weight, truck_weights):
    queue = deque(truck_weights)
    bridge = deque([0 for _ in range(bridge_length)])
    time, bridge_weight = 0, 0

    while len(queue) or bridge_weight > 0:
        time += 1
        truck_del = bridge.popleft()
        bridge_weight -= truck_del

        if len(queue) and bridge_weight + queue[0] <= weight:
            truck_add = queue.popleft()
            bridge_weight += truck_add
            bridge.append(truck_add)
        else:
            bridge.append(0)

    return time