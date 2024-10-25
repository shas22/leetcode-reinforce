class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(key = lambda e: len(e))

        res = []

        for f in folder:
            flag = True

            for i in range(2, len(f)):
                if f[i] == '/' and f[:i] in res:
                    flag = False

                    break
                
            if flag:
                res.append(f)

        return res
