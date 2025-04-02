def main():
    import sys

    N, *L = map(int, sys.stdin.read().split())
    
    found = {l: [] for l in L}
    check = set()
    need = sorted(L, reverse=True)
    
    last_num = -1
    last_length = 0
    
    while need:
        last_num = (last_num + 1) << (need[-1] - last_length) 
        b = f'{last_num:0{need[-1]}b}'
        if b in check or len(b) > need[-1]:
            sys.stdout.write('-1')
            exit(0)
        check.add(b)
        found[need.pop()].append(b)
        last_length = len(b)
        
    
    sys.stdout.write('1\n' + '\n'.join(found[l].pop() for l in L))


if __name__ == '__main__':
    main()