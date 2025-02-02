import sys
import re

raw = sys.stdin.readline().rstrip()
p = re.compile(r'<|>|&&|\|\||\(|\)|[^ <>&|()]+')
print(' '.join(p.findall(raw)))