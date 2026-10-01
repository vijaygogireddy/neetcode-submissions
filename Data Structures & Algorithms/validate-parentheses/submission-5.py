class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        parMap = {'}':'{', ')':'(', ']':'['}
        
        for char in s:
            if char not in parMap:
                arr.append(char)
            elif arr and parMap[char] == arr[-1]:
                arr.pop()
            else: return False

        return True if not arr else False

            # ([{}])
            # ([{[}])




        