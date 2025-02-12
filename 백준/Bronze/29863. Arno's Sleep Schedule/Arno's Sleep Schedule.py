sleep, wakeup = int(input()), int(input())
if wakeup < sleep:
    wakeup += 24
print(wakeup - sleep)