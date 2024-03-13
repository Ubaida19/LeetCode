import math
def pivot_integer(n:int)->int:
    x = math.sqrt(n(n+1)//2)
    if x==int(x):
        return x
    else:
        return -1
def main():
    print(pivot_integer(8))
    print(pivot_integer(13))
main()