def main():
    import sys
    
    sys.setrecursionlimit(100000)
    
    lines = iter(sys.stdin.read().rstrip().splitlines())
    
    Q = map(int, next(lines))
    A = {'^': None, '?': None, '+': 0}
    B = {'^': None, '?': None, '+': 0}
    results = []

    for line in lines:
        op, arg1, *args = line.split()
        if op == 'add':
            if arg1 == 'A':
                cur = A
                string = args[0]
            else:
                cur = B
                string = args[0][::-1]
            
            for cha in string:
                cur['+'] += 1
                if cha not in cur:
                    cur[cha] = {'^': cur, '?': cha, '+': 0}
                cur = cur[cha]
            cur['+'] += 1
            cur['@'] = None
            
        elif op == 'delete':
            if arg1 == 'A':
                cur = A
                string = args[0]
            else:
                cur = B
                string = args[0][::-1]
            
            for cha in string:
                cur = cur[cha]
            del cur['@']
            cur['+'] -= 1
            
            while cur['+'] == 0 and cur['^'] is not None:
                parent, cha = cur['^'], cur['?']
                del parent[cha]
                cur = parent
                cur['+'] -= 1
            while cur['^'] is not None:
                cur = cur['^']
                cur['+'] -= 1
        
        else:
            string = arg1
            A_depth_to_word_count = [0] * (len(string) - 1)
            cur = A
            for i, cha in enumerate(string[:-1]):
                if cha not in cur:
                    break
                cur = cur[cha]
                A_depth_to_word_count[i] = cur['+']
            
            B_depth_to_word_count = [0] * (len(string) - 1)
            cur = B
            for i, cha in enumerate(string[::-1][:-1]):
                if cha not in cur:
                    break
                cur = cur[cha]
                B_depth_to_word_count[i] = cur['+']
            
            results.append(sum(a * b for a, b in zip(A_depth_to_word_count, B_depth_to_word_count[::-1])))

    sys.stdout.write('\n'.join(map(str, results)))


if __name__ == '__main__':
    main()