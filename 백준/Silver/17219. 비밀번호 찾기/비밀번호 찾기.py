import sys

m, n = map(int, sys.stdin.readline().split())

accounts = dict()
for _ in range(m):
    server, password = sys.stdin.readline().split()
    accounts[server] = password
    
for _ in range(n):
    server = sys.stdin.readline().rstrip()
    sys.stdout.write(accounts[server] + '\n')