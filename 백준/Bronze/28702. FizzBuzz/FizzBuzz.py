pattern = (input(), input(), input())

def fizz_buzz(x):
    x_5 = x % 5 == 0
    if x % 3 == 0:
        if x_5:
            return 'FizzBuzz'
        else:
            return 'Fizz'
    elif x_5:
        return 'Buzz'
    return str(x)  

found = None
for i, p in enumerate(pattern):
    try:
        found = int(p)
        offset = 3 - i
    except:
        continue

if found:
    print(fizz_buzz(found + offset))
else:
    x = 0
    queue = []
    while True:
        x += 1  
        queue.append(fb)
        if len(queue) < 4:
            continue
        if (queue[0], queue[1], queue[2]) == pattern:
            print(queue[4])
            break
        queue.pop[0]
