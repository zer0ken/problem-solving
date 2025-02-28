for i in range(1, int(input()) + 1):
    if i != 1:
        print()
    input()
    print(f'Case {i}: This list contains {input().split().count('sheep')} sheep.')