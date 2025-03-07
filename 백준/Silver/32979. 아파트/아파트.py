def main():
    import sys
    from collections import deque
    
    읽어봐 = sys.stdin.readline
    써봐 = sys.stdout.write
    
    읽어봐()
    읽어봐()
    
    아파트 = deque(읽어봐().split())
    몇층 = list(map(int, 읽어봐().split()))
    
    for 층 in 몇층:
        아파트.rotate(-층 + 1)
        패배자 = 아파트[0]
        써봐(f'{패배자}\n')


if __name__ == '__main__':
    main()