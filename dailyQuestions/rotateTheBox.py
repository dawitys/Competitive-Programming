class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:        
        for i in range(len(box)-1,-1,-1):
            for j in range(len(box[0])-1,-1,-1):
                if(box[i][j] == "#"):
                    potentialPlace = j
                    while(potentialPlace + 1 < len(box[0]) and box[i][potentialPlace + 1] != "#" and box[i][potentialPlace + 1] != "*"):
                        potentialPlace += 1
                    box[i][j] = "."
                    box[i][potentialPlace] = "#"
                    
        res = [[box[i][j] for i in range(len(box)-1,-1,-1)] for j in range(len(box[0]))]
        return res
