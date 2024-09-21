""" 

Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
Return the new length of the array. Do not allocate extra space for another array; you must do this by modifying the input array in-place.

"""

def removeDuplicates(nums):
    if not nums:
        return 0
    i = 0
    
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i + 1 
    
    
nums = [1, 1, 2, 3, 4, 4, 4, 5]
new_length = removeDuplicates(nums)
print("The new length is:", new_length)
print("The array with duplicates removed:", nums[:new_length])
