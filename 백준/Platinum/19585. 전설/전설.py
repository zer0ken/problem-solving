def main():
    import sys

    lines = iter(sys.stdin.read().rstrip().splitlines())
    
    C, N = map(int, next(lines).split())
    
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.is_terminal = False
    
    color_trie = TrieNode()
    for _ in range(C):
        color = next(lines)
        
        cur = color_trie
        for cha in color:
            if cha not in cur.children:
                cur.children[cha] = TrieNode()
            cur = cur.children[cha]
        cur.is_terminal = True

    names = {next(lines) for _ in range(N)}

    Q, *queries = lines
    results = []

    for query in queries:
        cur = color_trie
        
        possible_names = []
        for i in range(len(query)):
            if cur.is_terminal:
                possible_names.append(query[i:])
            if query[i] not in cur.children:
                break
            cur = cur.children[query[i]]
        
        if any(name in names for name in possible_names):
            results.append('Yes')
        else:
            results.append('No')

    sys.stdout.write('\n'.join(results))


if __name__ == '__main__':
    main()