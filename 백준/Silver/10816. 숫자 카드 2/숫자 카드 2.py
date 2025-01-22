import sys
from collections import Counter

lines = sys.stdin.read().split('\n')
counter = Counter(lines[1].split())
sys.stdout.write(' '.join([str(counter[v]) for v in lines[3].split()]))