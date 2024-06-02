def sortArray(nums):
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2
    left_portion = nums[:mid]
    right_portion = nums[mid:]

    left_portion = sortArray(left_portion)
    right_portion = sortArray(right_portion)

    return merge(left_portion, right_portion)

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1

        else:
            result.append(right[right_idx])
            right_idx += 1

    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    return result



arr1 = [5, 2, 3, 1]

arr2 = [5, 1, 1, 2, 0, 0]

print(sortArray(arr1))
print(sortArray(arr2))