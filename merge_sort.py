
def partition(nums, length):
    first = nums[:length]
    second = nums[length:]
    return first, second

def merge(s1, s2, nums):
    i = 0
    j = 0
    tracker = 0
    n = len(nums)
    while i < len(s1) and j < len(s2):
        if s1[i] <= s2[j]:
            nums[tracker] = s1[i]
            i = i + 1
        else:
            nums[tracker] = s2[j]
            j = j + 1
        tracker = tracker + 1
    while i < len(s1):
        nums[tracker] = s1[i]
        i = i + 1
        tracker = tracker + 1
    while j < len(s2):
        nums[tracker] = s2[j]
        j = j + 1
        tracker = tracker + 1


def merge_sort(nums):
    if len(nums) > 1:
        length = len(nums) // 2
        s1, s2 = partition(nums, length)
        merge_sort(s1)
        merge_sort(s2)
        nums = merge(s1, s2, nums)
