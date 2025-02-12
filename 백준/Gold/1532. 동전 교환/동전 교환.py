def main():
    import sys
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    G1, S1, B1 = map(int, readline().split())
    G2, S2, B2 = map(int, readline().split())
    
    step = 0
    g, s, b = G1, S1, B1
    while g < G2:
        g += 1
        s -= 11
        step += 1
    while s < S2:
        if g > G2:
            g -= 1
            s += 9
        else:
            s += 1
            b -= 11
        step += 1
    while b < B2:
        if s > S2:
            s -= 1
            b += 9
            step += 1
        elif g > G2:
            g -= 1
            s += 8
            b += 9
            step += 2
        else:
            write('-1')
            exit(0)
    write(str(step))


if __name__ == '__main__':
    main()