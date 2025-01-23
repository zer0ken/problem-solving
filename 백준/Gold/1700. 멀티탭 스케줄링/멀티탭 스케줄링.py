import sys
readline = sys.stdin.readline

N, K = map(int, readline().split())
arr = readline().split()

usage = dict()
for i, device in enumerate(arr):
    if device not in usage:
        usage[device] = []
    usage[device].append(i)

removal = 0
multitab = []
for device in arr:
    usage[device].pop(0)
    if device in multitab:
        continue
        
    if len(multitab) < N:
        multitab.append(device)
        continue
    
    next_reuse = 0
    to_discard = 0
    for i, using_device in enumerate(multitab):
        if not usage[using_device]:
            to_discard = i
            break
        if usage[using_device][0] > next_reuse:
            next_reuse = usage[using_device][0]
            to_discard = i
    
    multitab[to_discard] = device
    removal += 1

sys.stdout.write(str(removal))