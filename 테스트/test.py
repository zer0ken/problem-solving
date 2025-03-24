import sys

N_K, *lines = sys.stdin.read().rstrip().splitlines()
N, K = map(int, N_K.split())
knapsack = [0] * (K + 1)
for line in lines:
    W, V = map(int, line.split())
    for i in range(K, W - 1, -1):
        if knapsack[i] < knapsack[i-W] + V:
            knapsack[i] = knapsack[i-W] + V
sys.stdout.write(str(max(knapsack)))