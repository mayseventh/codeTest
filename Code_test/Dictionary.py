# 사전(Dictionary) 사용 예제
score = {
    'match': 97,
    'eng': 49,
    'kor': 89
}

print(score['match'])

if 'music' in score:
    print(score['music'])
else:
    score['music'] = 30

print(score['music'])

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

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

class Solution(object):
    def __init__(self):
        self.dic = {}

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in nums:
            self.dic[i] = "true"
            check = target - i
            print("check is {0}".format(check))
            print("dic is {0}".format(self.dic))
            
            # dic에 포함 여부 및 중복 사용 여부 체크
            # dictionary에서 존재 여부 체크해야 O(n) 시간복잡도로 해결 가능
            if check in self.dic and check != i:
                return True
        return False

# nums=[4,1,9,7,5,3,16]
nums = [4,1,9,7,8,2]
target = 14

sol = Solution()
print(sol.twoSum(nums, target))




