def main():
    import sys
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N = int(readline())
    cranes = sorted(map(int, readline().split()), reverse=True)
    M = int(readline())
    boxes = sorted(map(int, readline().split()), reverse=True)

    if boxes[0] > cranes[0]:
        write('-1')
        exit(0)
    
    time = 0
    while boxes:
        time += 1
        for i, crane in enumerate(cranes):
            used = 0
            for j, box in enumerate(boxes):
                if box <= crane:
                    used = 1
                    boxes.pop(j)
                    break
            if not boxes:
                break
            if not used:
                cranes = cranes[:i]
                break
    write(str(time))


if __name__ == '__main__':
    main()