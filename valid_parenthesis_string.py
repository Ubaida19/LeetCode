def check_valid_string(s:str)->bool:
    lo = hi = 0
    for c in s:
        lo += 1 if c == '(' else -1
        hi += 1 if c != ')' else -1
        if hi < 0:
            break
        lo = max(lo, 0)
    return lo == 0


def main():
    s1 = "()"
    print(check_valid_string(s1))

    s2 = "(*)"
    print(check_valid_string(s2))

    s3 = "(*))"
    print(check_valid_string(s3))

    s4 = "(*))("

if __name__ == "__main__":
    main()