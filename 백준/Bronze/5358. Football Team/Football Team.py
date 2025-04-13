import sys
print(sys.stdin.read().translate(str.maketrans('ieIE', 'eiEI')))
