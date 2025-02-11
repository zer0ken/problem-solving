values = {
    'Franklin': 100, 
    'Grant': 50, 
    'Jackson': 20, 
    'Hamilton': 10, 
    'Lincoln': 5, 
    'Washington': 1
}
for _ in range(int(input())):
    print(f'${sum(map(lambda x: values[x], input().split()))}')