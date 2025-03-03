class Solution:
    def decode_recursively(self, string, start):
        decoded = ''
        k = ''
        i = start
        while i < len(string):
            c = string[i]
            if ord('0') <= ord(c) <= ord('9'):
                k += c
            elif c == '[':
                substr, end = self.decode_recursively(string, i + 1)
                decoded += substr * int(k)
                k = ''
                i = end
            elif c == ']':
                break
            else:
                decoded += c
            i += 1
        return decoded, i
    
    def decodeString(self, string: str) -> str:
        return self.decode_recursively(string, 0)[0]