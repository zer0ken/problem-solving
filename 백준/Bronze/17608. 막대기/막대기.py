def main():
    import sys

    N = int(sys.stdin.readline())
    stack = []
    for _ in range(N):
        l = int(sys.stdin.readline())
        while stack and stack[-1] <= l:
            stack.pop()
        stack.append(l)
    sys.stdout.write(str(len(stack)))

if __name__ == '__main__':
    main()