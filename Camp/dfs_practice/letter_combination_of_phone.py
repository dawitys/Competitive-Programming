class Solution: 
    def letterCombinations(self, digits: str) -> List[str]:
        digitToLetter = {
                        "2":"abc",  "3":"def",
                        "4":"ghi",  "5":"jkl", "6":"mno",
                        "7":"pqrs", "8":"tuv", "9":"wxyz"
                        }
        paths = set()
        def dfs(index,tempStr):
            if(index == len(digits)-1):
                for letter in digitToLetter[digits[index]]:
                    paths.add("".join(tempStr + [letter]))
                return   

            for letter in digitToLetter[digits[index]]:
                dfs(index + 1,tempStr + [letter])
        
        if(len(digits)>0):
            dfs(0,[])

        return list(paths)
