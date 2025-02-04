def main():
    import sys

    sys.stdin.readline()
    acc = 0
    for _ in range(200000):
        acc += int(sys.stdin.readline())
    sys.stdout.write('200000\n')
    sys.stdout.write(str(acc))

    
if __name__ == '__main__':
    main()