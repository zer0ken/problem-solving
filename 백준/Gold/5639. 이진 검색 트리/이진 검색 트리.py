def main():
    import sys
    sys.setrecursionlimit(100000)
    INF = float('inf')
    read = sys.stdin.read
    write = sys.stdout.write

    values = list(map(int, read().rstrip().split()))
    
    tree = []
    
    def build_tree(i, min_, max_):
        if i == len(values) or not min_ < values[i] < max_:
            return [], i
        node = [values[i]]
        i += 1
        
        left_node, i = build_tree(i, min_, node[0])
        right_node, i = build_tree(i, node[0], max_)
        
        node.append(left_node)
        node.append(right_node)
        
        return node, i
    
    def print_postorder_traversal(node):
        if not node:
            return
        print_postorder_traversal(node[1])
        print_postorder_traversal(node[2])
        write(f'{node[0]}\n')
    
    tree, _ = build_tree(0, -INF, INF)
    print_postorder_traversal(tree)


if __name__ == '__main__':
    main()