a, _, b, _, c = input().split()
d, _, e, _, f = input().split()

a, b, c, d, e, f = map(int, (a, b, c, d, e, f))

start = a*60*60 + b*60 + c
end = d*60*60 + e*60 + f

print((end - start) % (24*60*60))