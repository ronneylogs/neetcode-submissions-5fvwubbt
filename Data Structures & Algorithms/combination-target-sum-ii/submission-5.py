class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # Initialize array to store values
        res = []

        # Sort the candidates so duplicates are next to eachother
        candidates.sort()

        # DFS function to traverse the tree
        def dfs(i,path,total):
            # Base case 1 (target reached)
            if total == target:
                res.append(path.copy())
                return

            # Base case 2 (conditions breached)
            if i==len(candidates) or total>target:
                return

            
            # Add item
            path.append(candidates[i])

            # Recursive call
            dfs(i+1,path,total + candidates[i])

            # Subtract item
            path.pop()

            # Increment index so we don't run into duplicate
            while(i+1<len(candidates) and candidates[i]==candidates[i+1]):
                i = i+1
            
            # Recursive call
            dfs(i+1,path,total)

        dfs(0,[],0)
        return res
        