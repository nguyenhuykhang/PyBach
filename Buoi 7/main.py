# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array


class Solution:
    def majorityElement(self, nums: list[int]) -> int:

        for i in list:
            max = 0
            x = list.count(i)
            if x > max:
                max = x
                check = i
        return check, max

if __name__ == '__main__':
    list = [1, 1, 3, 3, 3, 4, 5, 6, 4, 4, 4, 4]
    p = Solution()
    print(p.majorityElement(list))




