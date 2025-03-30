def solution(land, P, Q):
    from bisect import bisect_left
    
    N, M = len(land), len(land[0])
    
    flat = []
    for row in land:
        flat.extend(row)
    flat.sort()
    
    possible_h = list(sorted(set(flat)))[1:]
    
    last_h = min(flat)
    base_cost = (sum(flat) - len(flat) * last_h) * Q
    costs = [base_cost]

    for target_h in possible_h:
        left = bisect_left(flat, target_h)
        right = len(flat) - left
        h_diff = target_h - last_h
        costs.append(costs[-1] + left*h_diff*P - right*h_diff*Q)
        last_h = target_h
        
    return min(costs)
