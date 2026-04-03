class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for i in range(len(nums)):
            l = i + 1
            r = len(nums)-1

            while(l<r):

                if (nums[i]+nums[l]+nums[r]==0):
                    res.add((nums[i],nums[l],nums[r]))
                    l += 1
                    r -= 1
                
                elif (nums[i]+nums[l]+nums[r]>0):
                    r -= 1
                
                else:
                    l += 1
            
        return list(res)
 

# Input is array
# Output is a list of lists where each inner list is a triplet containing numbers that add to 0

# Brute force would be to create a nested for loop, then for every pair we try a third number
    # But this would be very unefficient and take 

# Efficient way is to have an outer for loop and to anchor down on one element
    # Then for each inner number, we test numbers that work via the two pointer method
        # where we have a l and r pointer and increment based on our value

    # The idea is that moving the l pointer makes the sum bigger
        # and moving the r pointer makes the sum smaller





        



        