class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReq = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preReq[crs].append(pre)
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            
            visiting.add(crs)

            for p in preReq[crs]:
                if not dfs(p):
                    return False
        
            visiting.remove(crs)

            return True
            

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True



    
    # Create a prerequisite table
    # course: prerequisites

    # Keep a visited set
        # if visited then return false
    # Run dfs on each course
    # In the dfs, add current node to visited set and visit all neighbours