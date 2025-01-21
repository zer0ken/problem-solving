import sys
n = int(sys.stdin.readline().rstrip())
sys.stdout.write(f'{n} is {"odd" if n % 2 else "even"}')