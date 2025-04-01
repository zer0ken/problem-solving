decode = 'abcdefghijklmnopqrstuvwxyz '

for _ in range(int(input())):
    words = input().split()
    decoded = []
    for word in words:
        t = (sum(map(ord, word)) - 97*len(word)) % 27
        decoded.append(decode[t])
    print(''.join(decoded))