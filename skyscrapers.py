'''
Skyscrapers
https://github.com/karakumm/skyscrapers
'''
def read_input(path: str):
    """
    Read game board file from path.
    Return list of str.
    """

    with open(path) as file_:
        lines = file_.readlines()

    for index, line in enumerate(lines):
        lines[index] = line.rstrip()

    return lines


def left_to_right_check(input_line: str, pivot: int):
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is visible \
looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 5)
    False
    """
    rez = 0
    current = 0

    for num in input_line[1:-1]:
        num = int(num)
        if num > current:
            current = num
            rez += 1

    if rez == pivot:
        return True
    return False

def check_not_finished_board(board: list):
    """
    Check if skyscraper board is not finished, i.e., '?' present on the game board.

    Return True if finished, False otherwise.

    >>> check_not_finished_board(['***21**', '4?????*', '4?????*', '*?????5', \
'*?????*', '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*543215', \
'*35214*', '*41532*', '*2*1***'])
    True
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*5?3215', \
'*35214*', '*41532*', '*2*1***'])
    False
    """
    for row in board:
        for el_ in row:
            if el_ == '?':
                return False
    return True


def check_uniqueness_in_rows(board: list):
    """
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique length, False otherwise.

    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*543215', \
'*35214*', '*41532*', '*2*1***'])
    True
    >>> check_uniqueness_in_rows(['***21**', '452453*', '423145*', '*543215', \
'*35214*', '*41532*', '*2*1***'])
    False
    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*553215', \
'*35214*', '*41532*', '*2*1***'])
    False
    """
    for row in board[1:-1]:
        row = list(row[1:-1])

        while '*' in row:
            row.remove('*')
        if len(set(row)) != len(row):
            return False
    return True



def check_horizontal_visibility(board: list):
    """
    Check row-wise visibility (left-right and vice versa)

    Return True if all horizontal hints are satisfiable,
     i.e., for line 412453* , hint is 4, and 1245 are the four buildings
      that could be observed from the hint looking to the right.

    >>> check_horizontal_visibility(['***21**', '412453*', '423145*', \
'*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*', '423145*', \
'*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*', '423145*', \
'*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    result = set()
    for row in board[1:-1]:
        if row[0] != '*':
            input_line = row
            pivot = int(row[0])

            result1 = left_to_right_check(input_line, pivot)
            result.add(result1)

        row = row[::-1]
        if row[0] != '*':
            input_line = row
            pivot = int(row[0])

            result2 = left_to_right_check(input_line, pivot)
            result.add(result2)
    return all(result)


def check_columns(board: list):
    """
    Check column-wise compliance of the board for uniqueness (buildings of unique height)
    and visibility (top-bottom and vice versa).
    Same as for horizontal cases, but aggregated in one function for vertical case, i.e. columns.

    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', \
'*41532*', '*2*1***'])
    True
    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', \
'*41232*', '*2*1***'])
    False
    >>> check_columns(['***21**', '412553*', '423145*', '*543215', '*35214*', \
'*41532*', '*2*1***'])
    False
    """
    columns = []
    col = ''
    for i in range(len(board)):
        for row in range(len(board[i])):
            col += board[row][i]
        columns.append(col)
        col = ''

    if check_uniqueness_in_rows(columns) and check_horizontal_visibility(columns):
        return True

    return False


def check_skyscrapers(input_path: str):
    """
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.

    """
    board = read_input(input_path)

    if check_not_finished_board(board):
        return True
    elif check_uniqueness_in_rows(board):
        return True
    elif check_horizontal_visibility(board):
        return True
    elif check_columns(board):
        return True
    return False
