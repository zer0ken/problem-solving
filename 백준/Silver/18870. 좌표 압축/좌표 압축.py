def main():
    import sys
    
    N, *arr = map(int, sys.stdin.read().split())
    compressed = {v: i for i, v in enumerate(sorted(set(arr)))}
    sys.stdout.write(' '.join(map(str, (compressed[v] for v in arr))))


if __name__ == '__main__':
    main()