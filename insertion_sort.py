def insertion_sort(nums):
	for i in range(1, len(nums)):
		temp = nums[i]
		j = i
		while j > 0 and nums[j -1] > temp:
			nums[j] = nums[j -1]
			j = j - 1
		nums[j] = temp


	