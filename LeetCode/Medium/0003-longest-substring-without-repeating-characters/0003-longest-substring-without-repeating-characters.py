class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        p1 = 0
        p2 = 1
        max_len = 1
        characters = {s[0]}
        while p2 < len(s):
            if s[p2] not in characters:
                characters.add(s[p2])
                p2 += 1
                if max_len < len(characters):
                    max_len = len(characters)
            else:
                characters.remove(s[p1])
                p1 += 1
        return max_len