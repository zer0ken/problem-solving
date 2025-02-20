def main():
    import sys
    from bisect import bisect_left
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N, Q = map(int, readline().split())
    difficulties = list(map(int, readline().split()))
    for _ in range(Q):
        must_solve = int(readline())

        problems = []
        lis = []
        for problem, difficulty in enumerate(difficulties, 1):
            idx = bisect_left(lis, difficulty)
            if idx == len(lis):
                lis.append(difficulty)
                problems.append(problem)
            else:
                if problem == must_solve:
                    lis[idx] = difficulty
                    problems[idx] = problem
                    for _ in range(idx + 1, len(lis)):
                        lis.pop()
                        problems.pop()
                elif problems[idx] != must_solve:
                    lis[idx] = difficulty
                    problems[idx] = problem

        write(f'{len(lis)}\n')


if __name__ == '__main__':
    main()