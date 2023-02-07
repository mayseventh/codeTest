
# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

# 시간복잡도 O(n^2)
def two_Sum(nums, target):
    n=len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == 14:
                print("i is {0}, j is {1}, target is {2}".format(nums[i], nums[j], nums[i]+nums[j]))
                return True
    return False

print(two_Sum(nums=[4,1,9,7,5,3,16], target=14))

