class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        d={}
        for row in score:
            d[row[k]]=row
        keys = list(d.keys())
        keys.sort(reverse=True)
        return [d[row] for row in keys]