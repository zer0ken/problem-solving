def main():
    import sys
    import os
    
    total = 0
    numbers, _, left = os.read(0, 10101).decode('utf-8').rpartition('\n')
    numbers = numbers.split('\n')
    i = len(numbers) - 1
    map_of_numbers = map(int, numbers)
    map_of_numbers.__next__()
    total += sum(map_of_numbers)

    while i < 499330:
        temp = left
        numbers, _, left = os.read(0, 12921).decode('utf-8').rpartition('\n')
        if not temp and not numbers:
            break
        numbers = (temp + numbers).split('\n')
        i += numbers.__len__()
        total += sum(map(int, numbers))

    sys.stdout.write(i.__str__() + '\n' + total.__str__())

main()