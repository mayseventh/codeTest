
# 전체 시간복잡도는 O(nlogn)

def two_Sum(nums, target):
    nums.sort() # 정렬의 시간복잡도 O(nlogn)    
    n=len(nums)

    l, r = 0, n-1

    # while의 시간복잡도 O(n)
    while(l<r):
        print("l is {0}, r is {1}".format(l,r))
        if nums[l] + nums[r] > target:
            r -= 1
        elif nums[l] + nums[r] < target:
            l += 1
        elif nums[l] + nums[r] == target:
            return True
    return False

# print(two_Sum(nums=[4,1,9,7,5,3,16], target=14))
print(two_Sum(nums=[2,1,5,7], target=4))

