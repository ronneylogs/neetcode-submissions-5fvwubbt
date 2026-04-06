class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)


        visiting = set()
        def dfs(crs):
            if crs in visiting:
                return False
            
            visiting.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)

            return True

        # run dfs on each course
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True










        # build a graph where each course points to its prerequisits
        # Use a visit set to track the current DFS path
        # for each course:
            # run dfs
            # if the course is already in visiting, return false (cycle)
            # recursively dfs its prerequisites
        # after successfully processing a course, clear its prerequisite list (mark as done)
        # if all courses are processed without cycles, return true

        # Algorithm
        #     Build a graph where each course points to its prerequisites.
        #     Use a visiting set to track the current DFS path.
        #     For each course:
            #     Run DFS.
            #     If the course is already in visiting, return false (cycle).
            #     Recursively DFS its prerequisites.
        #     After successfully processing a course, clear its prerequisite list (mark as done).
        #     If all courses are processed without cycles, return true.