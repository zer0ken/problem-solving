def main():
    import sys
    from bisect import bisect_right
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N = int(readline())
    cranes = sorted(map(int, readline().split()))
    M = int(readline())
    boxes = sorted(map(int, readline().split()))

    if boxes[-1] > cranes[-1]:
        write('-1')
        exit(0)
    
    time = 0
    while boxes:
        time += 1
        for i in range(N - 1, -1, -1):
            crane = cranes[i]
            j = bisect_right(boxes, crane) - 1
            if j == -1:
                continue
            boxes.pop(j)
            if not boxes:
                break
    
    write(str(time))


if __name__ == '__main__':
    main()