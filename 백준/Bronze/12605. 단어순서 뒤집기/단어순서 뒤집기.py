import sys

for t in range(int(sys.stdin.readline())):
    sentence = sys.stdin.readline().split()
    sys.stdout.write(f'Case #{t + 1}: {" ".join(sentence[::-1])}\n')