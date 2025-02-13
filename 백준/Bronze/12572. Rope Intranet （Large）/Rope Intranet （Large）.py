def main():
    import sys
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    for t in range(1, int(readline()) + 1):
        N = int(readline())
        wires = [tuple(map(int, readline().split())) for _ in range(N)]
        count = 0
        for i in range(N - 1):
            s, e = wires[i]
            for j in range(i + 1, N):
                s_, e_ = wires[j]
                if (s - s_) * (e - e_) < 0:
                    count += 1
        write(f'Case #{t}: {count}\n')


if __name__ == '__main__':
    main()