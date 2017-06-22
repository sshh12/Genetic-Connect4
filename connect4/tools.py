
MAX = 999999
MIN = -MAX

def most_vertical(board, id_):
    rows, cols = board.shape
    most = 0
    for c in range(cols):
        for r in range(rows):
            if board[r, c] == id_:
                cnt = 1
                while r + cnt < rows and board[r + cnt, c] == id_:
                    cnt += 1
                most = max(most, cnt)
    return most

def most_horizontal(board, id_):
    rows, cols = board.shape
    most = 0
    for c in range(cols):
        for r in range(rows):
            if board[r, c] == id_:
                cnt = 1
                while c + cnt < cols and board[r, c + cnt] == id_:
                    cnt += 1
                most = max(most, cnt)
    return most

def most_inc_diagonal(board, id_):
    rows, cols = board.shape
    most = 0
    for c in range(cols):
        for r in range(rows):
            if board[r, c] == id_:
                cnt = 1
                while r - cnt > 0 and c + cnt < cols and board[r - cnt, c + cnt] == id_:
                    cnt += 1
                most = max(most, cnt)
    return most

def most_dec_diagonal(board, id_):
    rows, cols = board.shape
    most = 0
    for c in range(cols):
        for r in range(rows):
            if board[r, c] == id_:
                cnt = 1
                while r + cnt < rows and c + cnt < cols and board[r + cnt, c + cnt] == id_:
                    cnt += 1
                most = max(most, cnt)
    return most
