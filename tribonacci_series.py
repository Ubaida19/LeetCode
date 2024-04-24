def tribonacci(n:int) -> int:
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        tribonacci_series = [0] * 38
        tribonacci_series[0] = 0
        tribonacci_series[1] = 1
        tribonacci_series[2] = 1

        for i in range(3, n+1):
            tribonacci_series[i] = tribonacci_series[i-1] + tribonacci_series[i-2] + tribonacci_series[i-3]
            if i == n:
                return tribonacci_series[i]


def main():
    print(tribonacci(4))
    print(tribonacci(25))


main()
