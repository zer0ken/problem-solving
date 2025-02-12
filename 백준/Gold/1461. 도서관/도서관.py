def main():
    import sys
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N, M = map(int, readline().split())
    
    pos = []
    neg = []
    for d in map(int, readline().split()):
        if d < 0:
            neg.append(d)
        else:
            pos.append(d)
    pos.sort()
    neg.sort(reverse=True)
    
    steps = 0
    pos_far = pos[-1] if pos else 0
    pos_far2 = pos[max(0, len(pos) - 1 - M)] if pos else 0
    neg_far = abs(neg[-1]) if neg else 0
    neg_far2 = abs(neg[max(0, len(neg) - 1 - M)]) if neg else 0
     
    if pos_far > neg_far or (pos_far == neg_far and pos_far2 >= neg_far2):
        steps += pos_far
        for _ in range(min(M, len(pos))):
            pos.pop()
    else:
        steps += neg_far
        for _ in range(min(M, len(neg))):
            neg.pop()
    
    while pos:
        steps += 2 * pos[-1]
        for _ in range(min(M, len(pos))):
            pos.pop()
    
    while neg:
        steps -= 2 * neg[-1]
        for _ in range(min(M, len(neg))):
            neg.pop()
    
    write(str(steps))


if __name__ == '__main__':
    main()