def main():
    import sys
    write = sys.stdout.write
    
    N = int(input())
    last = ['*', '* *', '*****']
    
    for i in range(N):
        write(' ' * (N - i - 1))
        if i == len(last):
            gap = len(last[-1])
            last.extend(last[j] + ' '*(gap - 2*j) + last[j] for j in range(len(last)))
        write(last[i] + ' ' * (N - i - 1) + '\n')

if __name__ == '__main__':
    main()