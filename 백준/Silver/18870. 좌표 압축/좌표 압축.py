def main():
    import sys
    
    N, *arr = map(int, sys.stdin.read().split())
    
    compressed = {}
    last_v = None
    for i, v in enumerate(sorted(set(arr))):
        if i == 0 or last_v != v:
            compressed[v] = i
        last_v = v
    
    sys.stdout.write(' '.join(str(compressed[v]) for v in arr))


if __name__ == '__main__':
    main()