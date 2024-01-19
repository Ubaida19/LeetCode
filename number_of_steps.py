# https://leetcode.com/problems/climbing-stairs/description/?envType=daily-question&envId=2024-01-18
def main():
    """Driver code""" 
    steps = int(input('Enter the number of steps: '))
    print(climb_stairs(steps))
    
    
def climb_stairs(steps:int)->int:
    if steps <= 2:
        return steps
    first_step = 1
    second_step = 2
    result:int = 0
    for i in range(2,steps):
        result = first_step + second_step
        first_step = second_step
        second_step =result
        
    return result
        
if __name__ == '__main__':
    main()