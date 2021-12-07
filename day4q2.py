file = open("inputs/day4.txt", "r")

number_line = file.readline()
called_nums = number_line.split(",")
called_nums = [int(i) for i in called_nums]

def board_complete(board):
    for i in board:
        if sum(i) == -5: return True

    # transpose board
    board = list(zip(*board))
    for i in board:
        if sum(i) == -5: return True 

    return False

def point_complete_at(board):
    for index, called_num in enumerate(called_nums):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == called_num:
                    board[i][j] = -1
                    if board_complete(board.copy()):
                        return index

best_board = None
best_score = -1
print(called_nums)
best_board_index = 0
curr_index = 0
while True:
    if file.readline() == "":
        break

    lines_read_in_game = 0
    current_board = []
    while lines_read_in_game < 5:
        line = file.readline()
        

        if line.strip() == "":
            continue

        line = line.strip().split()
        numbers = [int(i) for i in line]
        current_board.append(numbers)
        lines_read_in_game += 1

    curr = point_complete_at(current_board.copy())
    if curr > best_score:
        best_board = current_board.copy()
        best_score = curr
        print("setting best score to:", best_score)
        best_board_index = curr_index
    curr_index += 1

print("called nums:", called_nums)
print("called num at best score:", called_nums[best_score])
best_sum = 0
for i in best_board:
    for j in i:
        if (j != -1):
            best_sum += j

print(best_sum)
print(best_sum*called_nums[best_score])
print(best_board_index)
print(best_board)