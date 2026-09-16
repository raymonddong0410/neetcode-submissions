class Solution:

    # the idea of this problem is to think of a way to delineate and also allocate
    # the range you need access to quickly
    # use attributes to your advantage --> length of a string and such
    # remember splicing

    # list of strings to a string --> no contraints on how it looks --> sent over network
    def encode(self, strs: List[str]) -> str:
        # can ask if only alphanumeric --> since checking only a char at a time can use isdigit or isalpha
        # otherwise use delimiter like #

        res = []
        for word in strs:
            res.append(str(len(word)))
            res.append("#")
            res.append(word)
        print(res)
        return "".join(res)
    
        
    # want to decode --> go through string and return back 
    # remember s is single string val so need a way to know where word ends --> ask what attribute of a string
    # specific char --> too complex and ambiguous
    # length more simple <-- use
    def decode(self, s: str) -> List[str]:
        res = []
        # for i in s:
        #     length = 

        # for loop not as useful as while loop since are skipping indices
        # number of iterations unknown/ looping whole thing not needed
        i = 0

        while i < len(s):
            # need another pointer to move forward
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res