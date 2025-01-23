import sys
from collections import Counter

word = sys.stdin.readline().rstrip().upper()

commons = Counter(word).most_common(2)
if len(commons) == 1:
    sys.stdout.write(commons[0][0])
elif commons[0][1] == commons[1][1]:
    sys.stdout.write('?')
else:
    sys.stdout.write(commons[0][0])