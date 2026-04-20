class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preMap = defaultdict(list)
        for crs in prerequisites:
            preMap[crs[0]].append(crs[1])

        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            
            visited.add(crs)
            for n in preMap[crs]:
                if dfs(n) == False:
                    return False
            visited.remove(crs)
            return True

        
        for crs in range(numCourses):
            if dfs(crs) == False:
                return False
        
        return True


        

        # create a dictionary
            # {course: [prereqs]}
        # iterate through each course then travel through each of the prereqs, i should not need to a visit 
            # a course that is already visited