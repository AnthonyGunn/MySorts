from merge_sort import partition, merge, merge_sort
from insertion_sort import insertion_sort

def hybrid_sort1(nums, H = -999):
    if H == -999:
        H = int(len(nums) ** (1/2))
    if len(nums) > H:
        S1, S2 = partition(nums, len(nums) // 2)
        hybrid_sort1(S1, H)
        hybrid_sort1(S2, H)
        merge(S1, S2, nums)
    else:
        insertion_sort(nums)

def hybrid_sort2(nums, H = -999):
    if H == -999:
        H = int(len(nums) ** (1/4))
    hybrid_sort1(nums, H)

def hybrid_sort3(nums, H = -999):
    if H == -999:
        H = int(len(nums) ** (1/6))
    hybrid_sort1(nums, H)



    
    