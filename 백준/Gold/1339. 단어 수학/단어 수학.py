def main():
    import sys
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N = int(readline())
    words = [readline().rstrip() for _ in range(N)]
    
    counter = {}
    for word in words:
        for i, cha in enumerate(word[::-1]):
            count = 10 ** i
            if cha in counter:
                counter[cha] += count
            else:
                counter[cha] = count
    
    sorted_counter = sorted(counter.items(), key=lambda item: item[1])
    to_num = {cha: i for i, cha in enumerate(map(lambda x: x[0], sorted_counter), 10 - len(counter))}
    
    max_len = max(map(len, words))
    for i in range(N):
        words[i] = ' ' * (max_len - len(words[i])) + words[i]
    
    result = 0
    for chars in zip(*words):
        result *= 10
        for char in chars:
            if char == ' ':
                continue
            result += to_num[char]
    
    write(str(result))


if __name__ == '__main__':
    main()