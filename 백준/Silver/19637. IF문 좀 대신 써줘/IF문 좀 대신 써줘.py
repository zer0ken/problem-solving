def main():
    import sys
    from bisect import bisect_left

    tokens = iter(sys.stdin.read().split())
    
    N, M = int(next(tokens)), next(tokens)
    
    score_upper_bounds = []
    titles = []
    
    for _ in range(N):
        title, score_upper_bound = next(tokens), int(next(tokens))
        score_upper_bounds.append(score_upper_bound)
        titles.append(title)
    
    results = []
    for score in map(int, tokens):
        results.append(titles[bisect_left(score_upper_bounds, score)])
    
    sys.stdout.write('\n'.join(results))


main()