import sys

sang, jung, ha, coke, soda = map(int, sys.stdin.read().split())
sys.stdout.write(str(min(sang, jung, ha) + min(coke, soda) - 50))