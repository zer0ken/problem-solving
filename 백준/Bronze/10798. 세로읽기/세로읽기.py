import sys

readline = sys.stdin.readline

lines = []
for _ in range(5):
    for i, cha in enumerate(readline().rstrip()):
        if i >= len(lines):
            lines.append('')
        lines[i] += cha
sys.stdout.write(''.join(lines))