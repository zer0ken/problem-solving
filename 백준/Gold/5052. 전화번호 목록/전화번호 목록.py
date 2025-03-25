def main():
    import sys
    
    lines = iter(sys.stdin.read().rstrip().splitlines())
    
    results = []
    for _ in range(int(next(lines))):
        N = int(next(lines))
        phones = [next(lines) for _ in range(N)] 
        phones.sort()
        for i in range(1, N):
            if phones[i].startswith(phones[i-1]):
                break
        else:
            results.append('YES')
            continue
        results.append('NO')
    
    sys.stdout.write('\n'.join(results))


if __name__ == '__main__':
    main()