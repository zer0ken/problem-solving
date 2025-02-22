import sys

word1 = sys.stdin.readline().rstrip()
word2 = sys.stdin.readline().rstrip()

l1 = len(word1)
l2 = len(word2)

matches = [[0] * (l2 + 1) for _ in range(l1 + 1)]
for i in range(1, l1 + 1):
    c1 = word1[i - 1]
    for j in range(1, l2 + 1):
        if word2[j - 1] == c1:
            matches[i][j] = max(matches[i][j-1], matches[i-1][j-1] + 1)
        else:
            matches[i][j] = max(matches[i][j-1], matches[i-1][j])

sys.stdout.write(str(matches[-1][-1]))