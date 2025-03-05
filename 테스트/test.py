def main():
    import sys
    write = sys.stdout.write
    
    N = int(input())
    last = ['*', '* *', '*****']
    
    for i in range(N):
        if i == len(last):
            gap = len(last[-1])
            last.extend(last[j] + ' '*(gap - 2*j) + last[j] for j in range(len(last)))
        spaces = ' ' * (N - i - 1)
        write(spaces + last[i] + spaces + '\n')

if __name__ == '__main__':
    main()