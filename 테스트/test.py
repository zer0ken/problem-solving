def main():
    import sys

    S, BADS, K = sys.stdin.read().split()
    K = int(K)
    ord_a = ord('a')

    prefix_sum = [0]
    for cha in S:
        prefix_sum.append(prefix_sum[-1] + int(BADS[ord(cha) - ord_a] == '0'))
    
    trie = {}
    count = 0
    for i in range(len(S)):
        cur = trie
        for j in range(i + 1, len(S) + 1):
            if prefix_sum[j] - prefix_sum[i] > K:
                break
            if S[j-1] not in cur:
                cur[S[j-1]] = {}
                count += 1
            cur = cur[S[j-1]]

    sys.stdout.write(str(count))


main()