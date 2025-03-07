class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ret = ''
        for s in map(set, zip(*strs)):
            if len(s) != 1:
                break
            ret += s.pop()
        return ret