def main():
    import sys
    from bisect import bisect_left
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N = int(readline())
    arr = list(map(int, readline().split()))

    top_of_each_stack = []
    for v in arr:
        idx = bisect_left(top_of_each_stack, v)
        if idx == len(top_of_each_stack):
            top_of_each_stack.append(v)
        else:
            top_of_each_stack[idx] = v

    write(str(len(top_of_each_stack)))


if __name__ == '__main__':
    main()