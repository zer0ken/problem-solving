import sys
s = sys.stdin.readline().rstrip()

ord_a = ord('a')

for cha in s:
    if ord(cha) < ord_a:
        sys.stdout.write(str.lower(cha))
    else:
        sys.stdout.write(str.upper(cha))