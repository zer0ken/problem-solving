import sys

readline = sys.stdin.readline

N, K = map(int, readline().split())
w_to_v = [0] * (K + 1)

for _ in range(N):
    w, v = map(int, readline().split())
    if w > K:
        continue
    for i in range(K, 0, -1):
        if w_to_v[i] != 0 and i + w <= K:
            w_to_v[i + w] = max(w_to_v[i + w], w_to_v[i] + v)
    w_to_v[w] = max(w_to_v[w], v)

sys.stdout.write(str(max(w_to_v)))