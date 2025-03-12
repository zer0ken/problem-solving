def main():
    import sys
    write = sys.stdout.write

    lines = sys.stdin.read().rstrip().splitlines()[:-1]
    for line in lines:
        A, B = map(int, line.split())
        a, b = A, B
        
        a_arr = [a]
        while a != 1:
            a = 3*a + 1 if a % 2 else a//2
            a_arr.append(a)
        
        b_arr = [b]
        while b != 1:
            b = 3*b + 1 if b % 2 else b//2
            b_arr.append(b)
        
        for i in range(-1, -min(len(a_arr), len(b_arr)) - 1, -1):
            if a_arr[i] != b_arr[i]:
                i += 1
                break
            
        write(f'{A} needs {len(a_arr) + i} steps, {B} needs {len(b_arr) + i} steps, they meet at {a_arr[i]}\n')


if __name__ == '__main__':
    main()