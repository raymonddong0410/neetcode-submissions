class Solution:

    # the idea of this problem is to think of a way to delineate and also allocate
    # the range you need access to quickly
    # use attributes to your advantage --> length of a string and such
    # remember splicing
    def encode(self, strs: List[str]) -> str:
        stringParts = []
        for word in strs:
            stringParts.append(str(len(word)))
            stringParts.append("#")
            stringParts.append(word)

        encodedString = "".join(stringParts)

        return encodedString

    def decode(self, s: str) -> List[str]:
        i = 0

        decodedString = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            # increment by 1 to get ahead of the #
            i = j + 1
            j = i + length
            decodedString.append(s[i:j])
            # continue from end of word
            i = j

        return decodedString