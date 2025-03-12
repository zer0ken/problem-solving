def main():
    import sys

    N = int(sys.stdin.readline())
    sum_dist = N**2 - 2*N + 1
    results = []
    for i in range(2, N + 1):
        results.append(f'1 {i}')

    sys.stdout.write(str(sum_dist) + '\n' + '\n'.join(results))


if __name__ == '__main__':
    main()