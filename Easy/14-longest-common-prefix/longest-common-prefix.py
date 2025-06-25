class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""
        i=0
        if not strs:
            return lcp
        while True:
            if i < len(strs[0]):
                lcp += strs[0][i]
            else:
                return lcp
                
            for string in strs[1:]:
                if i >= len(string) or string[i] != lcp[i]:
                    return lcp[:i]
            i+=1