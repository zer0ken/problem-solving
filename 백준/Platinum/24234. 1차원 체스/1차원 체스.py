def main():
    import sys
    from collections import defaultdict

    lines = iter(sys.stdin.read().rstrip().splitlines())
    N, Q = map(int, next(lines).split())

    trie = {}
    counter = defaultdict(lambda: 0)

    notation_sequences = [next(lines).split()[1:] for _ in range(N)]

    for notations in notation_sequences:
        cur = trie
        for notation in notations:
            if notation not in cur:
                cur[notation] = {'.notation': notation, '.descendants': 0}
            cur = cur[notation]
            cur['.descendants'] += 1
    
    for notations in notation_sequences:
        cur = trie
        for notation in notations:
            cur = cur[notation]

            if len(cur) <= 3 or '.visited' in cur:
                continue
            
            cur['.visited'] = None
            descendants = []
            for next_notation in cur:
                if next_notation[0] != '.':
                    descendants.append(cur[next_notation]['.descendants'])
            count = 0
            for i in range(len(descendants) - 1):
                for j in range(i + 1, len(descendants)):
                    count += descendants[i] * descendants[j]
            counter[cur['.notation']] += count

    print(*(counter[line] for line in lines), sep='\n')


if __name__ == '__main__':
    main()