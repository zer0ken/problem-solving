import sys

*lines, _ = sys.stdin.read().split()
results = []
for line in lines:
    results.append('yes' if line == line[::-1] else 'no')
sys.stdout.write('\n'.join(results))