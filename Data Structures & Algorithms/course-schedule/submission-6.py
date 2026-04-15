class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # create directed graph
        graph = defaultdict(list)
        for i in range(len(prerequisites)):
            course = prerequisites[i][0]
            prereq = prerequisites[i][1]
            graph[course].append(prereq)

        # 

        visited = set()
        def dfs(crs):
            # print(crs)
            if crs in visited:

                return False
            
            visited.add(crs)
            for n in graph[crs]:
          
                if dfs(n) == False:
               
                    return False
            
            visited.remove(crs)
            

            return

        # call dfs on every course
        for i in range(numCourses):
            if dfs(i) == False:
                return False
        
        return True


        
        


        # idea
        # the idea is just about detecting a cycle 
        # create a directed graph
        # {course:[prerequisites]}
        # use dfs, call every course. check if there is a cycle starting from every node

