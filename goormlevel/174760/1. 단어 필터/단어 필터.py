import re

ls, le = map(int, input().split())
s = input()
e = input()
while (m := re.search(s, e)):
    e = e[:m.start()] + e[m.end():]
print(e if e else 'EMPTY')