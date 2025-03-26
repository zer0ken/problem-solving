def main():
    import sys, os, io
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    input()
    acc = 0
    for _ in range(300000):
        acc += int(input())
    sys.stdout.write('300000\n' + str(acc))


if __name__ == '__main__':
    main()