def main():
    import sys
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N = int(readline())
    segments = [tuple(map(int, readline().split())) for _ in range(N)]
    segments.sort()
    
    X = []
    Y = []
    
    max_end = -1
    for i, segment in enumerate(segments):
        if max_end > segment[1]:
            Y.append(segment)
        else:
            X.append(segment)
            max_end = segment[1]
    
    
    def is_crossing(p1, p2):
        nonlocal segments, X, Y
        
        return (X[p1][0] - Y[p2][0]) * (X[p1][1] - Y[p2][1]) < 0
    
    
    def get_chain(p1, p2, looking_edges2):
        nonlocal X, Y
        
        chain = 2
        while p1 < len(X) and p2 < len(Y):
            if looking_edges2 and p2 < len(Y) - 1:
                if not is_crossing(p1, p2):
                    p1 -= 1
                    break
                elif is_crossing(p1, p2 + 1):
                    p2 += 1
                    chain += 1
                    looking_edges2 = not looking_edges2
                elif p1 < len(X) - 1:
                    p1 += 1
                else:
                    break
            elif not looking_edges2 and p1 < len(X) - 1:
                if not is_crossing(p1, p2):
                    p2 -= 1
                    break
                elif is_crossing(p1 + 1, p2):
                    p1 += 1
                    chain += 1
                    looking_edges2 = not looking_edges2
                elif p2 < len(Y) - 1:
                    p2 += 1
                else:
                    break
            else:
                break
        
        return chain, p1, p2
    
    
    max_chain = 1
    p1 = p2 = 0
    while p1 < len(X) and p2 < len(Y) and N - p1 - p2 > max_chain:
        if is_crossing(p1, p2):
            chain, p1, p2 = get_chain(p1, p2, looking_edges2=False)
            if max_chain < chain:
                max_chain = chain
            p1 += 1
            p2 += 1
        elif X[p1][0] < Y[p2][0]:
            p1 += 1
        else:
            p2 += 1
    
    p1 = p2 = 0
    while p1 < len(X) and p2 < len(Y) and N - p1 - p2 > max_chain:
        if is_crossing(p1, p2):
            chain, p1, p2 = get_chain(p1, p2, looking_edges2=True)
            if max_chain < chain:
                max_chain = chain
            p1 += 1
            p2 += 1
        elif X[p1][0] < Y[p2][0]:
            p1 += 1
        else:
            p2 += 1
    
    write(str(max_chain))


if __name__ == '__main__':
    main()