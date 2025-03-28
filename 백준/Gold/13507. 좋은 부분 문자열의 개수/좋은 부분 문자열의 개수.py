import sys

s, bads, k = sys.stdin.read().split()
k = int(k)
ord_a = ord('a')

prefix_sum = [0]
for cha in s:
    prefix_sum.append(prefix_sum[-1] + int(bads[ord(cha) - ord_a] == '0'))

good_strings = set()
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        if prefix_sum[j] - prefix_sum[i] <= k:
            seg = (i, j)
            good_strings.add(s[i:j])

print(len(good_strings))