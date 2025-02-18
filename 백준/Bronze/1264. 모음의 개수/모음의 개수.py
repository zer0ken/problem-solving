import sys
for line in sys.stdin.read().rstrip().lower().splitlines()[:-1]:
    print(sum(map(lambda v: line.count(v), 'aeiou')))