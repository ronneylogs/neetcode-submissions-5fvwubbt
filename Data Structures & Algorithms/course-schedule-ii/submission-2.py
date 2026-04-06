class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}
        res = []
        visiting = set()
        visited = set()

        for i in prerequisites:
            preMap[i[0]].append(i[1])
        
        def dfs(crs):
            # print(crs)
            if crs in visiting:
                return False
            
            if crs in visited:
                return True
            
            visiting.add(crs)
     
            for n in preMap[crs]:
                if dfs(n) == False:
                    return False
            
            visiting.remove(crs)

            visited.add(crs)
            res.append(crs)

            return True


        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return res