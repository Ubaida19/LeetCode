
def compareVersion(version1: str, version2: str) -> int:
    version1_list = version1.split('.')
    version2_list = version2.split('.')

    # Loop through both lists simultaneously
    for i in range(max(len(version1_list), len(version2_list))):
        # Get the integer value of revision i for both versions
        list1_ptr = int(version1_list[i]) if i < len(version1_list) else 0
        list2_ptr = int(version2_list[i]) if i < len(version2_list) else 0

        # Compare revisions
        if list1_ptr > list2_ptr:
            return 1
        elif list1_ptr < list2_ptr:
            return -1

    # If all revisions are equal, compareVersion numbers are equal
    return 0


def main():
    version1_1 = '1.001'
    version1_2 = '1.01'
    print(compareVersion(version1_1, version1_2))
    
    version2_1 = "1.0"
    version2_2 = "1.0.0"
    print(compareVersion(version2_1, version2_2))
    
    version3_1 = '0.1'
    version3_2 = '1.1'
    print(compareVersion(version3_1, version3_2))


if __name__ == "__main__":
    main()
    