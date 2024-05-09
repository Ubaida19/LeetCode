from typing import List


def maximum_happiness_sum(happiness: List[int], k: int) -> int:
    # Method 1
    happiness.sort(reverse=True)
    for i in range(k):
        happiness[i] = max(happiness[i]-i, 0)
    new_happiness = happiness[:k]
    return sum(new_happiness)

    # Method 2
    # happiness.sort(reverse=True)
    # happiness_sum = 0
    # i = 0
    # while k > 0:
    #     happiness[i] = max(happiness[i]-i, 0)
    #     happiness_sum += happiness[i]
    #     i += 1
    #     k -= 1
    # return happiness_sum


def main():
    happiness1 = [1, 2, 3]
    print(maximum_happiness_sum(happiness1, 2))

    happiness2 = [1, 1, 1, 1]
    print(maximum_happiness_sum(happiness2, 2))

    happiness3 = [2, 3, 4, 5]
    print(maximum_happiness_sum(happiness3, 1))

    happiness4 = [2, 83, 62]
    print(maximum_happiness_sum(happiness4, 3))

    happiness5 = [12, 1, 42]
    print(maximum_happiness_sum(happiness5, 3))

if __name__ == '__main__':
    main()
