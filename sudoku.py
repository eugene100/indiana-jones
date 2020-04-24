import random


def print_array(a):
    for row in a:
        for i in row:
            print i,
        print


def make_random_sudoku(size):
    res = []
    for i in range(0, size**2):
        p = range(1, size**2 + 1)
        random.shuffle(p)
        res.append(p)
    return res


def swap(row, a1, a2):
    row[a1], row[a2] = row[a2], row[a1]
    return row


def check_rows(sudoku, row):
    c = 0
    while c < len(row):
        r = len(sudoku) - 1
        nc = c
        status = False
        while not status:
            if row[c] == sudoku[r][c]:
                nc += 1
                if nc >= len(row):
                    return False
                else:
                    swap(row, c, nc)
                    r = len(sudoku) - 1
            else:
                r -= 1
                if r < 0:
                    status = True
        c += 1
    return status


def check_duplicate(p):
    # Checks array for duplicate items. Return true if duplacated items found.
    seen = []
    for i in p:
        if i in seen:
            return True
        else:
            seen.append(i)
    return False


def additional_check(sudoku, size):
    for pc in range(0, size):
        for pr in range(0, size):
            p = []
            if pc > 0:
                pass
            for i in range(pc*size, pc*size+size):
                for j in range(pr*size, pr*size+size):
                    p.append(sudoku[i][j])
            if check_duplicate(p):
                return False
    return True


def make_sudoku(size):
    sudoku = make_random_sudoku(size)
    i = 1
    while i < len(sudoku):
        if check_rows(sudoku[:i], sudoku[i]):
            i += 1
        else:
            if i > 1:
                i -= 1
            random.shuffle(sudoku[i])
    while not additional_check(sudoku, size):
        r1 = random.randint(0, len(sudoku) - 1)
        r2 = random.randint(0, len(sudoku) - 1)
        if random.randint(0, 1) == 1:
            if r1 == r2:
                sudoku = make_random_sudoku(size)
                # print 'New'
            # print '-',
            sudoku[r1], sudoku[r2] = sudoku[r2], sudoku[r1]
        else:
            for i in range(0, len(sudoku)):
                sudoku[i][r1], sudoku[i][r2] = sudoku[i][r2], sudoku[i][r1]
            # print '|',

    print '\nFound!'
    return sudoku


# print_array([[1,2,3,4],[3,4,1,2],[2,1,4,3],[4,3,2,1]])
print_array(make_sudoku(3))
