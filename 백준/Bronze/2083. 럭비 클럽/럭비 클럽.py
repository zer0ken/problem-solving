while True:
    name, age, weight = input().split()
    if name == '#' and age == '0' and weight == '0':
        exit(0)
    age, weight = int(age), int(weight)
    if age > 17 or weight >= 80:
        print(f'{name} Senior')
    else:
        print(f'{name} Junior')