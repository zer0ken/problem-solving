def main():
    import sys
    from collections import deque

    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N, start = readline().split()
    N = int(N)
    words = [readline().rstrip() for _ in range(N)]
    words.sort(key=len)
    queue = deque([words.index(start)])
    visited = [0] * N
    while queue:
        i = queue.popleft()
        word = words[i]
        l = len(word)
        has_no_next = 1
        for j, next_word in enumerate(words):
            if len(next_word) < l + 1:
                continue
            if len(next_word) > l + 1:
                break
            has_no_next = 0
            if visited[j]:
                continue
            for k, (s, e) in enumerate(zip(word, next_word)):
                if s != e:
                    break
            else:
                k += 1
            if word != next_word[:k] + next_word[k+1:]:
                continue
            visited[j] = 1
            queue.append(j)
        if has_no_next:
            break
    write(word)


if __name__ == '__main__':
    main()