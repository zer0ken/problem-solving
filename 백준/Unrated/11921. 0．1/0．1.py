def main():
    import sys
    import os

    total = 0
    numbers, _, left = os.read(0, 11500).decode('utf-8').rpartition('\n')
    numbers = numbers.split('\n')
    i = len(numbers) - 1
    map_of_numbers = map(int, numbers)
    map_of_numbers.__next__()
    total += sum(map_of_numbers)

    while i < 490000:
        if numbers == '':
            break
        temp = left
        numbers, _, left = os.read(0, 12000).decode('utf-8').rpartition('\n')
        numbers = temp + numbers
        numbers = numbers.split('\n')
        i += len(numbers)
        map_of_numbers = map(int, numbers)
        total += sum(map_of_numbers)

    sys.stdout.write(str(i) + '\n' + str(total))

main()