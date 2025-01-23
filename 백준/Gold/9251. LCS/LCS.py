import sys

readline = sys.stdin.readline
word1 = readline().rstrip()
word2 = readline().rstrip()

l1 = len(word1)
l2 = len(word2)

matches = [0] * (l2 + 1)

for i in range(l1):
    c1 = word1[i]
    for j in range(l2, 0, -1):
        last = matches[j - 1]
        if word2[j - 1] == c1:
            matches[j] = max(matches[j], last + 1)
        else:
            matches[j] = max(matches[j], last)
    for j in range(1, l2 + 1):
        matches[j] = max(matches[j - 1], matches[j])

sys.stdout.write(str(matches[-1]))