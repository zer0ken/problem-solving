import sys

M = int(sys.stdin.readline()) - 1

HYPER_GIMOSSI = 'Messi Messi Gimossi'
MESSI_GIMOSSI = 'Messi Gimossi'
messi = [5, 13]

while messi[-1] <= M:
    messi.append(messi[-1] + messi[-2] + 1)

idx = M
while idx > 12:
    if idx < messi[-2]:
        messi.pop()
        continue
    reduced_idx = idx - messi[-2] - 1
    idx = reduced_idx
    messi.pop()
    messi.pop()

if idx == -1 or MESSI_GIMOSSI[idx] == ' ':
    sys.stdout.write(HYPER_GIMOSSI)
else:
    sys.stdout.write(MESSI_GIMOSSI[idx])