class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        
        return res


    def decode(self, s: str) -> List[str]:
        
        i = 0
        out = []
        while i < len(s):
            n = ""
            while s[i] != "#":
                n += s[i]
                i += 1
            i += 1
        
            st = ''
            c = int(n)
            while c != 0:
                st += s[i]
                i += 1
                c -= 1
            out.append(st)

        return out


