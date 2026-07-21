class Solution(object):
    def isValid(self, s):
        # BRUTE FORCE O(n^2) SOLUTION
        #
        # while "()" in s or "{}" in s or "[]" in s:
        #     s = s.replace("()", "")
        #     s = s.replace("{}", "")
        #     s = s.replace("[]", "")
        # return s == ""


        # REAL SOLUTION O(n)
        stack = []
        close_open = {")" : "(", "}" : "{", "]" : "["}
        for char in s:
            if char in close_open:
                if stack and stack[-1] == close_open[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack