def solution(board):
    answer = []
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 1:
                board[i][j] = min(board[i - 1][j - 1], board[i][j - 1], board[i - 1][j]) + 1

    for i in range(len(board)):
        answer.append(max(board[i]))
    return max(answer) ** 2

# DP(Dynamic Programming) 동적 프로그래밍 이용