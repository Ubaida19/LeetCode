from typing import List


def count_students(students: List[int], sandwiches: List[int]) -> int:
    while sandwiches:
        if sandwiches[0] in students:
            students.remove(sandwiches[0])
            sandwiches.pop(0)
        else:
            return len(students)

    return 0

def main():
    students1 = [1, 1, 0, 0]
    sandwiches1 = [0, 1, 0, 1]
    print(count_students(students1, sandwiches1))

    students2 = [1, 1, 1, 0, 0, 1]
    sandwiches2 = [1, 0, 0, 0, 1, 1]
    print(count_students(students2, sandwiches2))


if __name__ == "__main__":
    main()