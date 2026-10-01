class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        parMap = {'}':'{', ')':'(', ']':'['}
        
        for char in s:
            if char in parMap:
                arr.append(char)
            elif arr and parMap[char] == arr[-1]:
                arr.pop()
            else: break

        return True if len(arr) == 0 else False

            # ([{}])
            # ([{[}])




        