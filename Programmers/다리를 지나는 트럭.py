from collections import deque

def solution(bridge_length,weight,truck_weights):
    truck_weights = deque(truck_weights)
    time = 0
    bridge = deque([0] * bridge_length)
    bridge_weight = 0
    while len(bridge) > 0:
        out = bridge.popleft()
        bridge_weight -= out
        time += 1
        if truck_weights:
            if truck_weights[0] + bridge_weight <= weight:
                popedleft = truck_weights.popleft()
                bridge_weight += popedleft
                bridge.append(popedleft)
            else:
                bridge.append(0)
    return time
    
            
    
solution(2,10,[7,4,5,6])

            
            
            
        