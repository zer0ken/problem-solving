import sys
import re

raw = sys.stdin.readline().rstrip()
p = re.compile(r'\+|\-|\d+')

pos = 0
neg = 0
do_subtract = False
for term in p.findall(raw):
    if term == '-':
        do_subtract = True
    elif term != '+':
        if do_subtract:
            neg += int(term)
        else:
            pos += int(term)

sys.stdout.write(str(pos-neg))