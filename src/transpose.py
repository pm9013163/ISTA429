def transpose(grid):
    retval = []
    for i in range(len(grid)):
        retval.append(get_col(grid,i))
    return retval
def get_col(grid,n):
    '''
    This function takes a multi-d list and returns
    a list of all values in a grid index. Function is recursive.
    N must be an integer smaller than the width of the grid
    '''
    if grid == []:
        return []
    elif len(grid) == 1:
        return [grid[0][n]]
    else:
        value = [grid[0][n]]
        new_grid = grid[1:]
