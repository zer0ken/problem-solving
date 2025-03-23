def main():
    import sys

    N, *lines = sys.stdin.read().rstrip().splitlines()
    
    row = [int(lines[0])]
    for i in range(1, int(N)):
        next_row = list(map(int, lines[i].split()))
        for j, v in enumerate(next_row):
            if j == 0:
                next_row[j] += row[j]
            elif j == i:
                next_row[j] += row[j-1]
            else:
                next_row[j] += max(row[j-1], row[j])
        row = next_row

    sys.stdout.write(str(max(row)))


if __name__ == '__main__':
    main()