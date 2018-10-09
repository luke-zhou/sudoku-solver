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
        print("row")
        for i in range(9):
            if need_evaluate(sudoku[i]):
                result, changed = evaluate(sudoku[i])
                sudoku[i] = result
                updated = updated or changed
        print_sudoku(sudoku)
        print(updated)
        print()


        print("column")
        sudoku = pivot(sudoku)
        for i in range(9):
            if need_evaluate(sudoku[i]):
                result, changed = evaluate(sudoku[i])
                sudoku[i] = result
                updated = updated or changed
        
        sudoku = pivot(sudoku)
        print_sudoku(sudoku)
        print(updated)
        print()

        print("square")
        sudoku = get_square(sudoku)
        for i in range(9):
            if need_evaluate(sudoku[i]):
                result, changed = evaluate(sudoku[i])
                sudoku[i] = result
                updated = updated or changed

        sudoku = get_square(sudoku)

        print_sudoku(sudoku)
        print(updated)
        print()


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
    # print("group:{}".format(group))
    
    for i in range(9):
        if type(group[i]) is list and len(group[i])==1:
            group[i] = group[i][0]


    nums = [e for e in group if type(e) is int]
    # nums.extend([e[0] for e in group if type(e) is list and len(e)==1])
    num_dict = {}
    new_group = [0]*9
    for i in range(9):
        if type(group[i]) is list:
            new_group[i] = [num for num in group[i] if num not in nums]
            # only element make it certain
            for e in new_group[i]:
                # print(e, i)
                # print(num_dict.items())
                num_dict[e] = num_dict[e]+[i] if e in num_dict else [i]
        else:
            new_group[i] = group[i]

    # print(new_group)
    # print(nums)
    # print(num_dict)

    if new_group == group:
        group_nums_count=2
        e_indexes = [i for i in range(9) if type(new_group[i]) is list and len(new_group[i])<=group_nums_count]
        indexes_length = len(e_indexes)
        if indexes_length >= group_nums_count:
            for i in range(indexes_length):
                for j in range(i+1, indexes_length):
                    if len(set(new_group[e_indexes[i]] + new_group[e_indexes[j]]))==group_nums_count:
                        print(new_group[e_indexes[i]], new_group[e_indexes[j]])
    
    if new_group == group:
        group_nums_count=3
        e_indexes = [i for i in range(9) if type(new_group[i]) is list and len(new_group[i])<=group_nums_count]
        indexes_length = len(e_indexes)
        if indexes_length >= group_nums_count:
            for i in range(indexes_length):
                for j in range(i+1, indexes_length):
                    for k in range(j+1, indexes_length):
                        if len(set(new_group[e_indexes[i]]+new_group[e_indexes[j]]+new_group[e_indexes[k]]))==group_nums_count:
                            # print(new_group[e_indexes[i]], new_group[e_indexes[j]],new_group[e_indexes[k]])
                            group_nums = set(new_group[e_indexes[i]]+new_group[e_indexes[j]]+new_group[e_indexes[k]])
                            for l in range(9):
                                if l not in [i,j,k] and type(group[l]) is list:
                                    new_group[l] = [num for num in new_group[l] if num not in group_nums]



    certain_nums = [k for k in num_dict if len(num_dict[k])
                    == 1 and k not in nums]
    for num in certain_nums:
        new_group[num_dict[num][0]] = num

    # print("new group:{}".format(new_group))
    return new_group, new_group != group


def print_sudoku(sudoku):
    for row in sudoku:
        # for e in row:
        #     print("{}\t".format(e),end='')
        # print()
        print(row)


if __name__ == "__main__":
    # result = evaluate([7, [1, 4], [1, 4, 5, 8], 3, [1, 4, 5, 8], 9, [4], [2, 4], 6])
    # print_sudoku(result)

    main(problem_hard)

    # list1 = [1,2,3]
    # list2 = [2,3,4]
    # print(set(list1+list2))

    # result = get_square(problem)
    # print_sudoku(result)
    # print()
    # result = get_square(result)
    # print_sudoku(result)
