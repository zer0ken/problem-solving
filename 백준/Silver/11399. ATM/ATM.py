import sys
waitings = map(int, sys.stdin.read().split('\n')[1].split())
sum_waiting = 0
acc = 0
for waiting in sorted(waitings):
    sum_waiting += waiting + acc
    acc += waiting
sys.stdout.write(str(sum_waiting))