class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = freq = longest = 0

        hashmap = defaultdict(int)

        for r in range(len(s)):
            hashmap[s[r]] += 1

            while (r-l+1 - max(hashmap.values())) > k:
                l += 1
                hashmap[s[l]] -= 1

            longest = max(longest, r-l+1)

        return longest









        '''
        counts = [0] * 26
        l = 0
        longest = 0
        for r in range(len(s)):
            counts[ord(s[r]) - 65] += 1

            while (r-l+1 - max(counts)) > k:
                counts[ord(s[l]) - 65] -= 1
                l += 1
            longest = max(longest, r-l+1)

            # ABABBAA k=2

        return longest
        '''