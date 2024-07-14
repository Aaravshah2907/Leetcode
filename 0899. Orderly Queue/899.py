class Solution:
    def orderlyQueue(self, s, k):
        n = len(s)

        if k > 1:
            ans = sorted(s)
            return "".join(ans)
        else:
            min_val = s 
            for i in range(n):
                s = s[1:] + s[0]
                min_val = min(min_val,s)
            return min_val