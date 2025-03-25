import sys

N, *words = sys.stdin.read().split()
words = list(set(words))
words.sort(key=lambda w: (len(w), w))
sys.stdout.write('\n'.join(words))