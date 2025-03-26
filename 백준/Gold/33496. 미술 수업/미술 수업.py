def main():
    import sys

    tokens = map(int, sys.stdin.read().split())
    
    N = next(tokens)
    lines = set()
    for _ in range(N):
        p, q = next(tokens), next(tokens)
        lines.add((p - q, 1))
        lines.add((p + q, -1))
    
    meet = 0
    ascending = 0
    last_x_intercept = -float('inf')
    for x_intercept, gradient in sorted(lines):
        if last_x_intercept != x_intercept:
            last_x_intercept = x_intercept
            meet += 1
        if gradient == 1:
            ascending += 1
        else:
            meet += ascending
    
    sys.stdout.write(str(meet))


main()