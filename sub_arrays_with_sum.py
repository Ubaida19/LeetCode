# def num_subarrays_with_sum(nums, goal)->int:
#     count = 0
#     prefix_sum = {0:1}
#     current_sum = 0
#     for num in nums:
#         current_sum+=num
#         count+=prefix_sum.get(current_sum-goal, 0)
#         prefix_sum[current_sum] = prefix_sum.get(current_sum,0) + 1
#     return count

def num_subarrays_with_sum(nums, goal):
    def at_most(goal):
            count = 0
            left = curr_sum = right = 0
            length = len(nums)
            for right in range(length):
                curr_sum += nums[right]
                while curr_sum > goal and left<=right:
                    curr_sum -= nums[left]
                    left += 1
                count += (right - left + 1)
            return count
    return at_most(goal) - at_most(goal-1)
def main():
    nums1 = [1, 0, 1, 0, 1]
    goal1 = 2
    print(num_subarrays_with_sum(nums=nums1,goal=goal1))
    
    nums2 = [0, 0, 0, 0, 0]
    goal2 = 0
    print(num_subarrays_with_sum(nums=nums2,goal=goal2))


if __name__ == "__main__":
    main()
    