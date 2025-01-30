import sys
input = sys.stdin.readline

def boj_10815():
    _, cards, _ = input(), set(input().split()), input()
    result = ''
    for card in input().split():
        if card in cards:
            result += '1 ' 
        else:
            result += '0 '
    print(result)

boj_10815()