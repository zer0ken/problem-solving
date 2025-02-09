def main():
    import sys
    import re
    from collections import deque

    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N, start = readline().split()
    N = int(N)
    id_to_word = []
    group_by_len = {}
    for i in range(N):
        word = readline().rstrip()
        l = len(word)
        if l in group_by_len:
            group_by_len[l].add(i)
        else:
            group_by_len[l] = {i}
        id_to_word[i] = word

    queue = deque([start])
    visited = [0] * N
    while queue:
        word = queue.popleft()
        l = len(word)
        if l + 1 not in group_by_len:
            write(word)
            exit(0)
        p = re.compile('^.?' + '.?'.join(word) + '.?$')
        for next_word in group_by_len[l + 1]:
            if visited[l + 1] and p.match(id_to_word[next_word]):
                visited[l + 1].add(next_word)
                queue.append(next_word)
    
    write(word)


if __name__ == '__main__':
    main()