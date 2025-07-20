class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        arr=[]
        for i in folder:
            if not arr or not i.startswith(arr[-1]+'/'):
                arr.append(i)
        return arr