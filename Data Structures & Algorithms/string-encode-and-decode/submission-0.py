class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            l = ''
            while s[i] != '#':
                l += s[i]
                i += 1
            
            i += 1

            st = ''
            c = int(l)
            while c != 0:
                st += s[i]
                i += 1
                c -= 1
            res.append(st)

        
        return res
            
