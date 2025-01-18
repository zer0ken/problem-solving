import sys
sys.stdout.write('\n'.join([line[::-1] for line in sys.stdin.read().split('\n')[1:]]))