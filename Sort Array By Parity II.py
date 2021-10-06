# 2 <= nums.length <= 2 * 104
# nums.length is even.
# Half of the integers in nums are even.
# 0 <= nums[i] <= 1000


class Solution:
    def sortArrayByParityII(self, nums):
        l = len(nums)
        output = [None] * l

        # 2 <= nums.length <= 2 * 104
        # nums.length is even.
        if len(nums) % 2 == 0 and len(nums) in range(2,208):

            ind = 0
            for i, x in enumerate(nums):
                # 0 <= nums[i] <= 1000
                if x < 0 or x > 1000:
                    print(False)
                elif x % 2 == 0:
                    output[ind] = x
                    ind += 2
                else:
                    return False

            ind = 1
            for i, x in enumerate(nums):
                # 0 <= nums[i] <= 1000
                if x < 0 or x > 1000:
                    print(False)
                elif x % 2 == 1:
                    output[ind] = x
                    ind += 2
                else:
                    return False
        return output





            # Half of the integers in nums are even.
            if len(even) == l/2:
                for i in range(int(l/2)):
                    output = output + [even[i]]
                    output = output + [odd[i]]
            else:
                print(False)
            return output
        else:
            print(False)




# Test
nums_1 = [4,2,5,7]

S = Solution()
S.sortArrayByParityII(nums_1)


# Better Solution
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        arr = [None]*len(nums)
        even,odd=0,1
        for i in nums:
            if not i%2:
                arr[even] = i
                even+=2
            else:
                arr[odd] = i
                odd+=2
        return arr