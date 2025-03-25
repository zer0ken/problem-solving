import sys

notes = sys.stdin.read().strip()
if notes == '1 2 3 4 5 6 7 8':
    sys.stdout.write('ascending')
elif notes == '8 7 6 5 4 3 2 1':
    sys.stdout.write('descending')
else:
    sys.stdout.write('mixed')