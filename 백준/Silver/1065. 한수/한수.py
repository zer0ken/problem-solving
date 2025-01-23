import sys

n = int(sys.stdin.readline().rstrip())
count = 0
for v in range(1, n + 1):
    if v < 100:
        count += 1
        continue
    digits = list(map(int, str(v)))
    d = digits[1] - digits[0]
    
    hansu = True
    for i in range(2, len(digits)):
        if digits[i] - digits[i-1] != d:
            hansu = False
            break
    
    if hansu:
        count += 1
sys.stdout.write(str(count))