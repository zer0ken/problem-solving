def solution(diffs, times, limit):
    
    lo = 1
    hi = max(diffs)
    
    while lo <= hi:
        mid = (lo + hi) // 2
        total_time = 0
        
        for i, (diff, time) in enumerate(zip(diffs, times)):
            fails = max(0, diff - mid)
            if fails:
                total_time += fails * (time + times[i-1])
            total_time += time
            
            if total_time > limit:
                break
        
        if total_time > limit:
            lo = mid + 1
        else:
            hi = mid - 1
    
    return lo