# https://leetcode.com/problems/longest-common-subsequence/description/?envType=daily-question&envId=2024-01-25
def main():
    print(longest_common_subsequence("abcde","ace"))
    print(longest_common_subsequence("abc","abc"))
    print(longest_common_subsequence("abc","def"))
    print(longest_common_subsequence("ezupkr","ubmrapg"))
    print(longest_common_subsequence("oxcpqrsvwf","shmtulqrypy"))
    
def longest_common_subsequence(text1:str, text2:str)->int:
    memo = {}
    return recursive(text1,text2,0,0,memo)
    
def recursive(text1,text2,i:int,j:int,memo)->int:
    if i == len(text1) or j == len(text2):
        return 0
    if (i,j) in memo:
        return memo[(i,j)]
    if text1[i] == text2[j]:
        memo[(i,j)] = 1 + recursive(text1, text2, i+1, j+1,memo)
    else:
        memo[(i,j)] = 0 + max(recursive(text1,text2,i+1,j,memo),recursive(text1,text2,i,j+1,memo))
    return memo[(i,j)]

if __name__ == '__main__':
        main()