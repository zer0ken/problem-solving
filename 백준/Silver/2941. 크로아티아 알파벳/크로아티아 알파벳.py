import sys

s = sys.stdin.readline().rstrip()
hsrvatska = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
i = 0
count = 0
while i < len(s):
    for alphabet in hsrvatska:
        if s[i:].startswith(alphabet):
            i += len(alphabet) -1
            break
    i += 1
    count += 1
sys.stdout.write(str(count))