from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    time = 0
    total = 0

    while bridge or truck_weights:
        time += 1
        total -= bridge.popleft()

        if truck_weights:
            if total + truck_weights[0] <= weight:
                truck = truck_weights.popleft()
                bridge.append(truck)
                total += truck
            else:
                bridge.append(0)

    return time
