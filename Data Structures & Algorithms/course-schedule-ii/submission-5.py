class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        seen = set()
        graph = defaultdict(list)
        done = set()
        for i in prerequisites:
            
            graph[i[0]].append(i[1])

        res = []

        def dfs(crs):
            if crs in done:
                return True
            if crs in seen:
                return False
            
            seen.add(crs)
            for n in graph[crs]:
                if dfs(n) == False:
                    return False

            seen.remove(crs)
            done.add(crs)
            if crs not in res:
                res.append(crs)
           

            return True
        

        for i in range(numCourses):
            if dfs(i) == False:
                return []
        
        return res