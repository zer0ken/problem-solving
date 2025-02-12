import sys
print('\n'.join(map(lambda x: f'{x} {x}', sys.stdin.read().rstrip().split('\n')[1:])))