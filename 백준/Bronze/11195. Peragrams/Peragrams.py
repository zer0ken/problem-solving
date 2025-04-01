from collections import Counter

counter = Counter(input())
odds = sum(count % 2 for count in counter.values())
print(max(0, odds - 1))