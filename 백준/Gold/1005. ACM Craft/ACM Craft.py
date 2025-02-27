def main():
    import sys
    readline = sys.stdin.readline
    write = sys.stdout.write
    TRUE, FALSE = 1, 0
    
    def solve():
        N, K = map(int, readline().split())
        D = [0] + list(map(int, readline().split()))
        graph = [[] for _ in range(N + 1)]
        incomming = [0] * (N + 1)
        for _ in range(K):
            X, Y = map(int, readline().split())
            graph[X].append(Y)
            incomming[Y] += 1
        W = int(readline())
        
        pre_cost = [0] * (N + 1)
        zero_incommings = []
        affected = set()
        while True:
            for i in range(1, N + 1):
                if incomming[i] == 0:
                    if i == W:
                        write(f'{D[i] + pre_cost[i]}\n')
                        return
                    zero_incommings.append(i)
                    incomming[i] = -1
            while zero_incommings:  
                done = zero_incommings.pop()
                for next_ in graph[done]:
                    affected.add(next_)
                    incomming[next_] -= 1
                    pre_cost[next_] = max(pre_cost[next_], D[done] + pre_cost[done])
            affected.clear()

    for _ in range(int(readline())):
        solve()

if __name__ == '__main__':
    main()