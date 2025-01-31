import sys

for _ in range(int(sys.stdin.readline())):
    money = int(sys.stdin.readline())
    quater = money // 25
    money %= 25
    dime = money // 10
    money %= 10
    nickel = money // 5
    penny = money % 5
    sys.stdout.write(f'{quater} {dime} {nickel} {penny}\n')