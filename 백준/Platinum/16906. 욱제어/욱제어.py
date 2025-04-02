def main():
    import sys

    N, *L = map(int, sys.stdin.read().split())
    
    stack = []
    trie = {}
    found = {l: [] for l in L}
    need = sorted(L, reverse=True)
    depth = 0

    while need:
        while depth < need[-1]:
            if '0' not in trie:
                stack.append('0')
                trie['0'] = {'parent': trie}
                trie = trie['0']
                depth += 1
            elif '1' not in trie:
                stack.append('1')
                trie['1'] = {'parent': trie}
                trie = trie['1']
                depth += 1
            elif 'parent' in trie:
                stack.pop()
                trie = trie['parent']
                depth -= 1
            else:
                sys.stdout.write('-1')
                exit(0)
        found[need.pop()].append(''.join(stack))
        stack.pop()
        trie = trie['parent']
        depth -= 1
    
    sys.stdout.write('1\n' + '\n'.join(found[l].pop() for l in L))


if __name__ == '__main__':
    main()