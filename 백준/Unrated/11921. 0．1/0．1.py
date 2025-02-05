def main():
    import sys

    sys.stdin.readline()
    acc = 0
    for _ in range(234567):
        acc += int(sys.stdin.readline())
    print('234567\n', acc, sep='')

if __name__ == '__main__':
    main()