def main():
    import sys
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    
    N = int(readline())
    edges = [tuple(map(int, readline().split())) for i in range(N)]
    edges.sort()
    
    edges1 = []
    edges2 = []
    
    max_end = -1
    for i, (start, end) in enumerate(edges):
        if max_end > end:
            edges2.append(i)
        else:
            edges1.append(i)
            max_end = end
    
    
    def is_crossing(p1, p2):
        nonlocal edges, edges1, edges2
        
        s1, e1 = edges[edges1[p1]]
        s2, e2 = edges[edges2[p2]]
        return s1 < s2 and e1 > e2 or s1 > s2 and e1 < e2        

    
    
    def get_chain(p1, p2, looking_edges2):
        nonlocal edges1, edges2
        
        print('===')
        print(f'L1: {edges1}')
        print(f'L2: {edges2}')
        print(f'{p1=}, {p2=}에서부터 체인 생성 시작')
        print('===')
        
        chain = 2
        while p1 < len(edges1) and p2 < len(edges2):
            print(f'L1: {edges1[p1]} -- L2: {edges2[p2]}')
            if looking_edges2 and p2 < len(edges2) - 1:
                print('L2에서 뽑는 중')
                if is_crossing(p1, p2):
                    if is_crossing(p1, p2 + 1):
                        p2 += 1
                        chain += 1
                        looking_edges2 = not looking_edges2
                        print(f'\tL1: {edges1[p1]} --> L2: {edges2[p2]} 연결 성공')
                    elif p1 < len(edges1) - 1:
                        print(f'\tL1: {edges1[p1]} --x L2: {edges2[p2 + 1]} 연결 실패')
                        p1 += 1
                    else:
                        print('\t더이상 연결할 수 없음')
                        break
                else:
                    print('\t더이상 연결할 수 없음')
                    p1 -= 1
                    break
            elif not looking_edges2 and p1 < len(edges1) - 1:
                print('L1에서 뽑는 중')
                if is_crossing(p1, p2):
                    if is_crossing(p1 + 1, p2):
                        p1 += 1
                        chain += 1
                        looking_edges2 = not looking_edges2
                        print(f'\tL1: {edges1[p1]} <-- L2: {edges2[p2]} 연결 성공')
                    elif p2 < len(edges2) - 1:
                        print(f'\tL1: {edges1[p1 + 1]} x-- L2: {edges2[p2]} 연결 실패')
                        p2 += 1
                    else:
                        print('\t더이상 연결할 수 없음')
                        break
                else:
                    print('\t더이상 연결할 수 없음')
                    p2 -= 1
                    break
            else:
                print('\t더이상 연결할 수 없음')
                break
        
        print(f'최종: L1: {edges1[p1]} -- L2: {edges2[p2]}')
        print(f'{p1=}, {p2=}에서부터 체인 생성 ')
        print(f'선분 체인: {chain}')
        return chain, p1, p2

    max_chain = 1
    p1 = p2 = 0
    while p1 < len(edges1) and p2 < len(edges2) and N - p1 - p2 > max_chain:
        if is_crossing(p1, p2):
            chain, p1, p2 = get_chain(p1, p2, looking_edges2=False)
            max_chain = max(max_chain, chain)
            p1 += 1
            p2 += 1
        elif edges1[p1] < edges2[p2]:
            p1 += 1
        else:
            p2 += 1
    
    p1 = p2 = 0
    while p1 < len(edges1) and p2 < len(edges2) and N - p1 - p2 > max_chain:
        if is_crossing(p1, p2):
            chain, p1, p2 = get_chain(p1, p2, looking_edges2=True)
            max_chain = max(max_chain, chain)
            p1 += 1
            p2 += 1
        elif edges1[p1] < edges2[p2]:
            p1 += 1
        else:
            p2 += 1
    
    write(str(max_chain))

if __name__ == '__main__':
    main()