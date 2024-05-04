from typing import List
def number_of_boats(people:List[int], limit:int)->int:
    people.sort()
    boat_count = 0
    right:int = len(people) - 1
    left:int = 0
    while left<=right:
        if people[right] + people[left] <= limit:
            left += 1
        right -= 1
        boat_count += 1
    return boat_count

def main():
    
    people = [5,1,4,2]
    limit = 6
    print(number_of_boats(people, limit))
    people1 = [1, 2]
    limit1 = 3
    
    print(number_of_boats(people1, limit1))
    
    people2 = [3,2,2,1]
    limit2 = 3
    print(number_of_boats(people2, limit2))
    
    people3 = [3,5,3,4]
    limit3 = 5
    print(number_of_boats(people3, limit3))
    
if __name__ == '__main__':
    main()