class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        file_dict = dict()
        folders = []
        for name in names:
            if(file_dict.get(name,0) == 0):
                file_dict[name]  = 1
                folders.append(name)
            else:
                candidate = file_dict[name]
                temp = "".join([name,'(',str(candidate),')'])
                while(temp in file_dict):
                    candidate += 1
                    temp = "".join([name,'(',str(candidate),')'])
                file_dict[temp] = 1
                folders.append(temp)
                file_dict[name] = candidate

        return folders
