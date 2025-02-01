import sys

x, y = map(int, sys.stdin.readline().split())

days = [28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
acc_days = [0, 0, 31]
for i in range(11):
    acc_days.append(acc_days[-1] + days[i])

total = acc_days[x] + y - 1
weekdays = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
sys.stdout.write(weekdays[total % 7])