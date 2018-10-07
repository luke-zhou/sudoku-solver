problem_hard = [
    [0, 0, 0, 0, 1, 7, 5, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 0, 0],
    [7, 4, 8, 0, 0, 0, 2, 0, 0],
    [8, 5, 4, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 2, 0],
    [0, 0, 0, 0, 4, 0, 1, 6, 0],
    [5, 0, 0, 8, 0, 0, 0, 7, 0],
    [0, 0, 0, 7, 0, 0, 0, 0, 9],
    [0, 6, 0, 0, 0, 9, 0, 0, 8]
]

problem_easy = [
    [7, 0, 0, 3, 0, 9, 0, 0, 6],
    [0, 2, 6, 0, 0, 0, 0, 1, 8],
    [0, 0, 0, 0, 2, 6, 7, 0, 0],
    [4, 8, 0, 0, 0, 0, 5, 0, 3],
    [0, 0, 2, 8, 9, 0, 0, 0, 0],
    [0, 9, 0, 7, 0, 3, 0, 8, 0],
    [0, 0, 9, 4, 0, 2, 3, 0, 0],
    [0, 0, 3, 9, 0, 0, 0, 5, 4],
    [1, 5, 0, 0, 0, 8, 2, 0, 0]
]


def main(problem):
    sudoku = preprocessing(problem)
    updated = True
    while updated:
        updated = False
        for _ in range(2):
            for i in range(9):
                if need_evaluate(sudoku[i]):
                    result, changed = evaluate(sudoku[i])
                    sudoku[i] = result
                    updated = updated or changed

            sudoku = pivot(sudoku)

        print_sudoku(sudoku)
        print(updated)
        print()

        sudoku = get_square(sudoku)
        for i in range(9):
            if need_evaluate(sudoku[i]):
                result, changed = evaluate(sudoku[i])
                sudoku[i] = result
                updated = updated or changed

        sudoku = get_square(sudoku)

        print_sudoku(sudoku)
        print(updated)


def get_square(sudoku):
    new_sudoku = [[0]*9 for i in range(9)]
    for i in range(9):
        for j in range(9):
            # print(i,j,int((i%3)/3)+int(j/3)+int(i/3)*3, (j%3+i*3)%9)
            new_sudoku[int((i % 3)/3)+int(j/3)+int(i/3) *
                       3][(j % 3+i*3) % 9] = sudoku[i][j]
            # print_sudoku(new_sudoku)

    return new_sudoku


def pivot(sudoku):
    new_sudoku = [[0]*9 for i in range(9)]
    for i in range(9):
        for j in range(9):
            # print(i, j, sudoku[i][j])
            new_sudoku[j][i] = sudoku[i][j]
            # print_sudoku(new_sudoku)

    return new_sudoku


def preprocessing(sudoku_problem):
    sudoku = sudoku_problem[:]
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                sudoku[i][j] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    return sudoku


def need_evaluate(group):
    return any([type(e) is list for e in group])


def evaluate(group):
    nums = [e for e in group if type(e) is int]
    num_dict = {}
    new_group = [0]*9
    for i in range(9):
        if type(group[i]) is list:
            new_group[i] = [num for num in group[i] if num not in nums]
            # only element make it certain
            if len(new_group[i]) == 1:
                new_group[i] = new_group[i][0]
                nums.append(new_group[i])
            else:
                for e in new_group[i]:
                    # print(e, i)
                    # print(num_dict.items())
                    num_dict[e] = num_dict[e]+[i] if e in num_dict else [i]
        else:
            new_group[i] = group[i]

    # print(new_group)

    certain_nums = [k for k in num_dict if len(num_dict[k])
                    == 1 and num_dict[k] not in nums]

    for i in range(9):
        if type(new_group[i]) is list:
            test_result = [num for num in group[i] if num in certain_nums]
            new_group[i] = test_result[0] if len(
                test_result) == 1 else new_group[i]

    return new_group, new_group != group


def print_sudoku(sudoku):
    for row in sudoku:
        print(row)


if __name__ == "__main__":
    # result = evaluate([3, 2, [1, 7], [5, 8], 5, 9, 6, 4, [1, 5, 7, 8]])
    # print_sudoku(result)

    main(problem_hard)

    # result = get_square(problem)
    # print_sudoku(result)
    # print()
    # result = get_square(result)
    # print_sudoku(result)
