def main():
    import sys
    from collections import deque
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N = int(readline())
    tree = [[] for _ in range(N)]
    root = -1
    for node, parent in enumerate(map(int, readline().split())):
        if parent == -1:
            root = node
        else:
            tree[parent].append(node)
    cut = int(readline())
    if cut == root:
        write('0')
        exit(0)
        
    terminals = 0
    queue = deque([root])
    while queue:
        node = queue.popleft()
        has_child = False
        for child in tree[node]:
            if child != cut:
                queue.append(child)
                has_child = True
        if not has_child:
            terminals += 1
    write(str(terminals))


if __name__ == '__main__':
    main()