def shell_sort1(nums):
    gap = len(nums) // 2
    while gap > 0:
        i = gap
        while i < len(nums):
            temp = nums[i]
            j = i
            while j >= gap and temp < nums[j - gap]:
                nums[j] = nums[j - gap]
                j = j - gap
            nums[j] = temp
            i = i + 1
        gap = gap // 2

# calculates the sequence(A083318) for shell sort 2 
def calc_sort2(list_length):
    result = [0, 1]
    for i in range(1, list_length):
        gap = 2**i + 1
        if gap < list_length:
            result.append(2**i + 1)
    result.reverse()
    return result

def shell_sort2(nums):
    gap_list = calc_sort2(len(nums))
    tracker = 0
    gap = gap_list[tracker]
    while gap > 0:
        i = gap
        while i < len(nums):
            temp = nums[i]
            j = i
            while j >= gap and temp < nums[j - gap]:
                nums[j] = nums[j - gap]
                j = j - gap
            nums[j] = temp
            i = i + 1
        if tracker <= len(gap_list):
            tracker = tracker + 1
            gap = gap_list[tracker]

# calculates the sequence(A003586) for shell sort 3
def calc_sort3(list_length):
    result = [0]
    for i in range(0, list_length):
        for j in range(0, list_length):
            gap = (2 ** i) * (3 ** j)
            if gap < list_length:
                result.append(gap)
            else:
                break
    result.reverse()
    return result

def shell_sort3(nums):
    gap_list = calc_sort3(len(nums))
    tracker = 0
    gap = gap_list[tracker]
    while gap > 0:
        i = gap
        while i < len(nums):
            temp = nums[i]
            j = i
            while j >= gap and temp < nums[j - gap]:
                nums[j] = nums[j - gap]
                j = j - gap
            nums[j] = temp
            i = i + 1
        if tracker <= len(gap_list):
            tracker = tracker + 1
            gap = gap_list[tracker] 

# calculates the sequence(A033622) for shell sort 4
def calc_sort4(list_length):
    hardcoded_sequence = [0,1,5,19,41,109,209,505,929,2161,3905,8929,16001,36289,64769,146305,260609,587521,1045505,2354689, 
    188161,9427969,16764929,37730305,67084289,
    150958081,268386305,603906049,1073643521,
    2415771649,4294770689,9663381505,17179475969]
    result = []
    for i in range(len(hardcoded_sequence)):
        gap = hardcoded_sequence[i]
        if gap < list_length:
            result.append(gap)
    result.reverse()
    return result

def shell_sort4(nums):
    gap_list = calc_sort4(len(nums))
    tracker = 0
    gap = gap_list[tracker]
    while gap > 0:
        i = gap
        while i < len(nums):
            temp = nums[i]
            j = i
            while j >= gap and temp < nums[j - gap]:
                nums[j] = nums[j - gap]
                j = j - gap
            nums[j] = temp
            i = i + 1
        if tracker <= len(gap_list):
            tracker = tracker + 1
            gap = gap_list[tracker]
