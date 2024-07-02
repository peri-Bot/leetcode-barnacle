def searchInsert(nums , target: int) -> int:
            low = 0
            mid = 0
            high = len(nums) - 1
            
            nums_dict = {str(value): index for index,value in enumerate(nums)}
            length = len(nums)

            while low <= high:
                mid = low + (high - low) // 2 

                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

            if target > nums[length - 1] and len(nums) != 1:
                return nums_dict[str(nums[length - 1])] + 1
            elif len(nums) == 1:
                return high + 1
            else:
                return low
