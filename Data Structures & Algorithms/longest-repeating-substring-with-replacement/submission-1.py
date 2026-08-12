class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        hm = defaultdict(int)
        count = 0
        maxf = 0

        for r in range(len(s)):
            hm[s[r]] += 1

            maxf = max(maxf, hm[s[r]])
            while (r - l + 1) - maxf > k:
                hm[s[l]] -= 1
                l += 1
            
            count = max(count, r - l + 1)

        
        return count


        