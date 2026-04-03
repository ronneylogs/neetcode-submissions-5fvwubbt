class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Put values in a tuple inside a list sorted on the first variable

        pair = [(p,s) for p,s in zip(position,speed)]
        pair.sort(reverse=True)

        stack = []

        for p,s in pair:
            curTime = (target-p)/s
            
            if len(stack)==0:
                stack.append(curTime)
            else:
                topTime = stack[-1]
                if curTime>topTime:
                    stack.append(curTime)

        return len(stack)
        