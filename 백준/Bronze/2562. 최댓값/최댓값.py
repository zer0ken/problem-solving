import sys

max_ = int(sys.stdin.readline().rstrip())
max_i = 1

for i in range(2, 10):
    v = int(sys.stdin.readline().rstrip())
    
    if v > max_:
        max_ = v
        max_i = i

sys.stdout.write(str(max_) + '\n' + str(max_i))