class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = {}
        maxLen = 0

        for r in range(len(s)):
            # want to move left pointer forward to where the last instance was seen + 1
            # --> min steps forward until we skip past the last we saw the repeat
            if s[r] in seen and seen[s[r]] >= l:
                l = seen[s[r]] + 1
            seen[s[r]] = r
            maxLen = max(maxLen, r - l + 1)

        return maxLen

