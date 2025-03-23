def main():
    import sys

    N, *arr = map(int, sys.stdin.read().split())
    sys.stdout.write(f'{min(arr)} {max(arr)}')


if __name__ == '__main__':
    main()