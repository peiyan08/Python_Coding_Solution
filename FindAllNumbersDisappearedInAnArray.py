"""448 Find All Numbers Disappeared in an Array

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
""" 

nums = [4,3,2,7,8,2,3,1]

for i in range(len(nums)):
        index = abs(nums[i]) - 1
        nums[index] = - abs(nums[index])

print [i + 1 for i in range(len(nums)) if nums[i] > 0]

#
index = 4-1 = 3
nums[3] = -7
index = 3 - 1 = 2
nums[2] = -2
index = 2 - 1 = 1
nums[1] = -3
index = 6
nums[6] = -3
index = 7
nums[7] = -1
index = 1
nums[1] = -3
index = 2
num[2] = -2
index = 0
num[0] = -4

