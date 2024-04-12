from typing import List


def trap(height: List[int]) -> int:
    n = len(height)
    # Indices to traverse the array
    left = 0
    right = n - 1

    # To store Left max and right max
    # for two pointers left and right
    l_max = 0
    r_max = 0

    # To store the total amount
    # of rain water trapped
    result = 0
    while left <= right:

        # We need check for minimum of left
        # and right max for each element
        if r_max <= l_max:

            # Add the difference between
            # current value and right max at index r
            result += max(0, r_max - height[right])

            # Update right max
            r_max = max(r_max, height[right])

            # Update right pointer
            right -= 1
        else:

            # Add the difference between
            # current value and left max at index l
            result += max(0, l_max - height[left])

            # Update left max
            l_max = max(l_max, height[left])

            # Update left pointer
            left += 1
    return result


def main():
    height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(trap(height1))

    height2 = [4, 2, 0, 3, 2, 5]
    print(trap(height2))


if __name__ == "__main__":
    main()
