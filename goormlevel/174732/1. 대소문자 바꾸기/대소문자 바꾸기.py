import sys

sys.stdin.readline()
arr = list(sys.stdin.readline().rstrip())

ord_a = ord('a')
ord_A = ord('A')
for i, c in enumerate(arr):
    ord_c = ord(c)
    if ord_c >= ord_a:
        arr[i] = chr(ord_c - ord_a + ord_A)
    else:
        arr[i] = chr(ord_c - ord_A + ord_a)
sys.stdout.write(''.join(arr))