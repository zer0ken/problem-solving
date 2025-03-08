class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [''] * numRows
        cur = 0
        is_ascending = True
        for c in s:
            rows[cur] += c
            if is_ascending:
                if cur == numRows - 1:
                    cur -= 1
                    is_ascending = False
                else:
                    cur += 1
            elif cur == 0:
                cur += 1
                is_ascending = True
            else:
                cur -= 1
        
        return ''.join(rows)
            