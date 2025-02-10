def main():
    import sys
    import re
    from collections import Counter, deque

    def is_todalin(start, end):
        for i, (s, e) in enumerate(zip(start, end)):
            if s != e:
                break
        else:
            i += 1
        return 1 if start == end[:i] + end[i+1:] else 0

    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N, start = readline().split()
    N = int(N)
    words = [readline().rstrip() for _ in range(N)]
    queue = deque([words.index(start)])
    visited = [0] * N
    while queue:
        i = queue.popleft()
        word = words[i]
        l = len(word)
        has_no_next = 1
        for j, next_word in enumerate(words):
            if len(next_word) == l + 1:
                has_no_next = 0
                if not visited[j] and is_todalin(word, next_word):
                    visited[j] = 1
                    queue.append(j)
        if has_no_next:
            break
    write(word)


if __name__ == '__main__':
    main()