class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        left = {}
        right = {}

        for i in range(len(t)):

            left[t[i]] = left.get(t[i], 0) + 1
            right[s[i]] = right.get(s[i], 0) + 1

            #the way get works is that it returns the value of left[t[i]] if
            #is there if not it set it to 0, we need the + 1 to count

        print(left)
        print(right)

        return left == right
        #if they have the same key - vlaue pairs then a anagram is there
