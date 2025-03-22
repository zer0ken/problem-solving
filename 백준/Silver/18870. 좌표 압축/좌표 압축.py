def main():
    import sys
    
    N, *arr = map(int, sys.stdin.read().split())
    
    compressed = {}
    for i, v in enumerate(sorted(set(arr))):
        if v not in compressed:
            compressed[v] = i
    
    sys.stdout.write(' '.join(str(compressed[v]) for v in arr))


if __name__ == '__main__':
    main()