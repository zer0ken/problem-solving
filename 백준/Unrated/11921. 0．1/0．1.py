def main():
    import sys
    import os

    total = 0
    numbers, _, left = os.read(0, 10010).decode('utf-8').rpartition('\n')
    numbers = numbers.split('\n')
    i = len(numbers) - 1
    map_of_numbers = map(int, numbers)
    map_of_numbers.__next__()
    total += sum(map_of_numbers)

    while i < 496022:
        temp = left
        numbers, _, left = os.read(0, 13600).decode('utf-8').rpartition('\n')
        numbers = temp + numbers
        numbers = numbers.split('\n')
        if numbers == '':
            break
        i += len(numbers)
        total += sum(map(int, numbers))

    sys.stdout.write(str(i) + '\n' + str(total))

main()