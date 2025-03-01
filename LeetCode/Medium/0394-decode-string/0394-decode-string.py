class Solution:
    def decodeString(self, string: str) -> str:
        k = ['']
        s = ['']
        for c in string:
            if ord('0') <= ord(c) <= ord('9'):
                k[-1] += c
            elif c == '[':
                k.append('')
                s.append('')
            elif c == ']':
                k.pop()
                t = s.pop() * int(k.pop())
                s[-1] += t
                k.append('')
            else:
                s[-1] += c
        return s[-1]
