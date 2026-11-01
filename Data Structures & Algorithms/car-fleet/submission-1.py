class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(z,y) for z,y in zip(position,speed)]
        pairs.sort(reverse=True)

        stack = []

        for p,s in pairs:
            curTime= (target-p) / s

            if len(stack)==0:
                stack.append(curTime)
            
            else:
                if curTime > stack[-1]:
                    stack.append(curTime)


        return len(stack)
        

        # monotonic stack: a stack where the items are increasing from bottom to the top of the stack

        # For each car, compute the time it will take to reach the target
        # cars that start closer to the target are processed first

        # if a car behidn reaches the target faster thant he car in front, it will eventuallyt catch up and join the same fleet
            # so we only keep the car's time if it forms a new fleet: otherwise it merged with the previous one


        # Algorithm
        # 1. Pair each car's position with its
        # 2. Sort the cars in descending order of position
        # 3. For each car:
            # Compute the time it takes to reach the target
            # Push this time onto a stack
            # If the new car's time is less than or equal to the time before it, it catches up and merges with that fleet -> pop from the stack
        # 4. The number of remaining times in the stack equals the number of fleets
        # 5. Return the stack size