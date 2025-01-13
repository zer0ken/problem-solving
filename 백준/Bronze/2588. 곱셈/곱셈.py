a = int(input())
b2, b1, b0 = input().strip()
r = (r0 := a * int(b0)) + (r1 := a * int(b1)) * 10 + (r2 := a * int(b2)) * 100
print(r0, r1, r2, r, sep='\n')