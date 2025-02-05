input = iter(open(0).read().split('\n')).__next__

N = int(input())
tanghulu = list(map(int,input().split()))

compressed = []
for tang in tanghulu:
    if compressed and compressed[-1][0] == tang:
        compressed[-1][1] += 1
    else:
        compressed.append([tang, 1])
M = len(compressed)
tanghulu = compressed

l = r = 0
count = [0] * 10
count[tanghulu[0][0]] = tanghulu[0][1]
max_count = 0
while l < M and r < M:
    if len(list(filter(lambda x: x > 0, count))) <= 2:
        total_count = sum(count)
        if max_count < total_count:
            max_count = total_count
        if r == M - 1:
            break
        r += 1
        count[tanghulu[r][0]] += tanghulu[r][1]
    else:
        count[tanghulu[l][0]] -= tanghulu[l][1]
        l += 1
print(max_count)