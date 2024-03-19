class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "": return []
        keys = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'}
        res = []

        def backtrack(curr, pos):
            if pos >= len(digits):
                res.append(curr.copy())
                return

            for i in keys[digits[pos]]:
                curr.append(i)
                backtrack(curr, pos + 1)
                curr.pop()

        backtrack([], 0)
        return [''.join(i) for i in res]
