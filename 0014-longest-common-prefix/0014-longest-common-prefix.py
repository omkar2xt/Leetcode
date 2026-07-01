class Solution:
    def longestCommonPrefix(self, strs):
        first = min(strs)
        last = max(strs)

        ans = ""

        for i in range(len(first)):
            if i < len(last) and first[i] == last[i]:
                ans += first[i]
            else:
                break

        return ans