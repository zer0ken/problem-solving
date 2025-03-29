def solution(diffs, times, limit):
    lo = 1
    hi = max(diffs)
    
    while lo <= hi:
        mid = (lo + hi) // 2
        
        total_time = 0
        for i, (diff, time) in enumerate(zip(diffs, times)):
            total_time += time
            if diff > mid:
                total_time += (diff - mid) * (time + times[i-1])
            if total_time > limit:
                break
        
        if total_time > limit:
            lo = mid + 1
        else:
            hi = mid - 1
    
    return lo