def main():
    import sys
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N, M = map(int, readline().split())
    boxes = []
    for _ in range(N):
        colors = set()
        for color, count in enumerate(map(int, readline().split())):
            if count > 0:
                colors.add(color)
        boxes.append(list(colors))
    
    min_moves = N
    for joker in range(N):
        has_own_box = [False] * M
        moves = 0
        for i in range(N):
            if i == joker or not boxes[i]:
                continue
            if len(boxes[i]) == 1:
                if has_own_box[boxes[i][0]]:
                    moves += 1
                else:
                    has_own_box[boxes[i][0]] = True
            else:
                moves += 1
        if min_moves > moves:
            min_moves = moves
    
    write(str(min_moves))


if __name__ == '__main__':
    main()