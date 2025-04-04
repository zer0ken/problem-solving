def main():
    import sys

    lines = iter(sys.stdin.read().rstrip().splitlines())
    results = []
    while lines:
        N = int(next(lines, 0))
        if N == 0:
            break
        words = [next(lines) for _ in range(N)]
        trie = {}
        
        for word in words:
            cur = trie
            for cha in word:
                if cha not in cur:
                    cur[cha] = {}
                cur = cur[cha]
            cur['@'] = None
        
        count = 0
        for word in words:
            count += 1
            cur = trie[word[0]]
            for cha in word[1:]:
                if '@' in cur or len(cur) != 1:
                    count += 1
                cur = cur[cha]
        results.append(count / N)
    
    sys.stdout.write('\n'.join(f'{avg:.2f}' for avg in results))


if __name__ == '__main__':
    main()