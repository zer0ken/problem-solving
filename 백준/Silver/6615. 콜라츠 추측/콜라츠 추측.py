def main():
    import sys
    import heapq

    readline = sys.stdin.readline
    write = sys.stdout.write
    
    lines = sys.stdin.read().rstrip().splitlines()[:-1]
    
    for line in lines:
        A, B = map(int, line.split())
        a, b = A, B
        
        a_arr = [a]
        while a != 1:
            a = 3*a + 1 if a % 2 else a//2
            a_arr.append(a)
        
        b_step = 0
        while b not in a_arr:
            b_step += 1
            b = 3*b + 1 if b % 2 else b//2
        write(f'{A} needs {a_arr.index(b)} steps, {B} needs {b_step} steps, they meet at {b}\n')


if __name__ == '__main__':
    main()