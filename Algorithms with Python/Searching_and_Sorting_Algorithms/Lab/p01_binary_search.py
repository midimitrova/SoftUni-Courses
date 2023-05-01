from unittest import TestCase, main


def binary_search(nums, target):
    left_idx = 0
    right_idx = len(nums) - 1
    while left_idx <= right_idx:
        mid_idx = (right_idx + left_idx) // 2

        if nums[mid_idx] == target:
            return mid_idx

        if target > nums[mid_idx]:
            left_idx = mid_idx + 1
        else:
            right_idx = mid_idx - 1
    return -1


nums = [int(x) for x in input().split()]
target = int(input())
print(binary_search(nums, target))

# class TestSearch(TestCase):
#
#     def test_is_list_empty(self):
#         self.assertEqual(-1, binary_search([], 2))
#         self.assertEqual(-1, binary_search([1, 2, 3], 5))
#
#
# if __name__ == '__main__':
#     main()
