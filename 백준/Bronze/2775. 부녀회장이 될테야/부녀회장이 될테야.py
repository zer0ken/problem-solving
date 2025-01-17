import sys

raw = sys.stdin.read().split()

residents = dict()

def get_residents(f, n):
    if f == 0:
        return n
    key = (f, n)
    if key in residents:
        return residents[key]

    resident = sum(get_residents(f - 1, i) for i in range(1, n + 1))
    residents[(f, n)] = resident
    return resident
    
for i in range(int(raw[0])):
    floor, number = int(raw[i*2 + 1]), int(raw[i*2 + 2])
    sys.stdout.write(str(get_residents(floor, number)) + '\n')
