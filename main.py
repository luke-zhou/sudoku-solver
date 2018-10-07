problem = [
    [6, 0, 0, 0, 1, 0, 8, 5, 0],
    [2, 0, 0, 0, 8, 5, 4, 0, 0],
    [8, 0, 5, 0, 0, 4, 1, 0, 0],
    [0, 0, 0, 4, 0, 2, 5, 0, 3],
    [0, 0, 2, 1, 3, 0, 0, 6, 0],
    [4, 0, 6, 0, 9, 0, 2, 0, 0],
    [3, 0, 0, 0, 0, 9, 6, 4, 0],
    [0, 0, 8, 7, 0, 1, 0, 2, 0],
    [5, 4, 0, 3, 2, 0, 0, 0, 0]
]


def main():
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
            new_sudoku[int((i%3)/3)+int(j/3)+int(i/3)*3][(j%3+i*3)%9] = sudoku[i][j]
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
                sudoku[i][j] = [1,2,3,4,5,6,7,8,9]
    
    return sudoku
    
def need_evaluate(group):
    return any([type(e) is list for e in group])

def evaluate(group):
    nums = [e for e in group if type(e) is int]
    num_dict ={}
    new_group = [0]*9
    for i in range(9):
        if type(group[i]) is list:
            new_group[i] =[num for num in group[i] if num not in nums]
            # only element make it certain
            if len(new_group[i])==1:
                new_group[i]=new_group[i][0]
            else:
                for e in new_group[i]:
                    num_dict[e] = num_dict[e]+1 if e in num_dict else 1
        else:
            new_group[i] = group[i]

    certain_nums =[k for k in num_dict if num_dict[k]==1]

    for i in range(9):
        if type(new_group[i]) is list:
            test_result = [num for num in group[i] if num in certain_nums]
            new_group[i]=test_result[0] if len(test_result)==1 else new_group[i]
    
    return new_group, new_group!=group


def print_sudoku(sudoku):
    for row in sudoku:
        print(row)

if __name__ == "__main__":
    # result = evaluate([6, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 1, [1, 2, 3, 4, 5, 6, 7, 8, 9], 8, 5, [1, 2, 3, 4, 5, 6, 7, 8, 9]])
    # print_sudoku(result)

    main()

    # result = get_square(problem)
    # print_sudoku(result)
    # print()
    # result = get_square(result)
    # print_sudoku(result)