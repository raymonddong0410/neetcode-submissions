class Solution:
    def isPalindrome(self, s: str) -> bool:
        # brute force would be to parse through the string, build the string with only alphanumeric
        # after building invert it and compare to see if they are the same

        # better method would just be to compare the left and right most and keep moving towards the middle
        # one pass and avoids building another string --> saves space

        if s == "":
            return True

        left = 0
        right = len(s) - 1

        # less than not if not equal in case where even number of chars
        while left < right:
            while left < right and not s[left].isalnum():
                # increment past non alpha numeric chars
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            # standardize so all lower
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True