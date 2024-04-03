from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    if not board:
        return False

    rows = len(board)
    cols = len(board[0])

    def dfs(row, col, word_idx):
        if word_idx == len(word):
            return True

        if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != word[word_idx]:
            return False

        temp = board[row][col]
        board[row][col] = '#'  # Mark as visited

        # Explore neighbors
        found = dfs(row + 1, col, word_idx + 1) or dfs(row - 1, col, word_idx + 1) or dfs(row, col + 1, word_idx + 1) or dfs(row, col - 1, word_idx + 1)

        board[row][col] = temp  # Reset the cell

        return found

    for row in range(rows):
        for col in range(cols):
            if dfs(row, col, 0):
                return True

    return False

def main():
    board1 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word1 = "ABCCED"
    print(exist(board1, word1))
    board2 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word2 = "SEE"
    print(exist(board2, word2))
    board3 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word3 = "ABCB"
    print(exist(board3, word3))

    board4 = [["a","a"]]
    word4 = "aaa"
    print(exist(board4, word4))


    board5 = [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]]
    word5 = "AAB"
    print(exist(board5, word5))


if __name__ == "__main__":
    main()