def main():
    import sys

    lines = iter(sys.stdin.read().rstrip().splitlines())
    
    C, N = map(int, next(lines).split())
            
    def create_trie_node():
        return {'is_terminal': False}
    
    color_trie = create_trie_node()
    for _ in range(C):
        color = next(lines)
        
        cur = color_trie
        for cha in color:
            if cha not in cur:
                cur[cha] = create_trie_node()
            cur = cur[cha]
        cur['is_terminal'] = True

    names = {next(lines) for _ in range(N)}

    Q, *queries = lines
    results = []

    for query in queries:
        cur = color_trie
        
        possible_names = []
        for i in range(len(query)):
            if cur['is_terminal']:
                possible_names.append(query[i:])
            if query[i] not in cur:
                break
            cur = cur[query[i]]

        if any(name in names for name in possible_names):
            results.append('Yes')
        else:
            results.append('No')

    sys.stdout.write('\n'.join(results))


if __name__ == '__main__':
    main()