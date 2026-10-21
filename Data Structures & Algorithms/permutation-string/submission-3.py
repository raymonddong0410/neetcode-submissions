class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # check whether s1 is longer than s2
        if len(s1) > len(s2):
            return False

        # idea is that we want to check the substring of only size of length of s1
        # however list splicing (brute force for me) is 0(n) so time complexity would be n^2
        # so instead do a comparison of a hashtable
        # do comparison incrementally because full comparison would be o(26) everytime here
        # this is also with the assumption that we are only using lowercase letters

        l1, l2 = len(s1), len(s2)
        s1Table = [0] * 26
        s2Table = [0] * 26

        # counter for number of matches --> required for incremental comparison
        numberOfMatches = 0

        for i in range(l1):
            s1Table[ord(s1[i]) - ord('a')] += 1
            # should also fill out the s2Table for initial comparison
            s2Table[ord(s2[i]) - ord('a')] += 1

        for i in range(26):
            if s1Table[i] == s2Table[i]:
                numberOfMatches += 1

        # intitial check before loop to see if number of matches is 26 --> if so means that substring exist
        if numberOfMatches == 26:
            return True

        # otherwise loop through and increment and decrement vals of tables to see if there is a match
        # start with index at next val
        # still want to stick with the initial window length
        l = 0
        for r in range(l1, l2):

            rightIdx = ord(s2[r]) - ord('a')
            s2Table[rightIdx] += 1
            if s2Table[rightIdx] == s1Table[rightIdx]:
                numberOfMatches += 1
            # use this condition because substring from right is being added in, vice versa for the other side of things
            elif s1Table[rightIdx] + 1 == s2Table[rightIdx]:
                numberOfMatches -= 1

            leftIdx = ord(s2[l]) - ord('a')
            s2Table[leftIdx] -= 1
            if s2Table[leftIdx] == s1Table[leftIdx]:
                numberOfMatches += 1
            elif s1Table[leftIdx] - 1 == s2Table[leftIdx]:
                numberOfMatches -= 1

            l+=1

            if numberOfMatches == 26:
                return True

        return False

            

