import copy
# add matrix to as a item in queue
size = 2
queue = []    # Open list # list of tuple [empty space location in matrix]
def disp(que):
    print(que)
    for row in que:
        for item in row:
            print(item, end=" ")
        print()
    print("\n\n")

def enqueue(curr_st):
    global queue
    queue.append(curr_st)
    # print(f"Enqueue = queue state is -> {disp(queue)}")

def dequeue():
    global queue
    if len(queue) > 0:
        front_st = queue[0]
        queue.pop(0)
        # print(f"Dequeue = queue state is -> {disp(queue)}")

        return front_st

def get_empty_space(matrix):
    for row_index, row in enumerate(matrix):
        for col_index, item in enumerate(row):
            if item == 0:
                return [row_index, col_index]


def top(curr_st, row_index, col_index):
    if row_index > 0:
        i = row_index-1

        curr_st[row_index][col_index], curr_st[i][col_index] = curr_st[i][col_index], curr_st[row_index][col_index]
    return curr_st

def bottom(curr_st, row_index, col_index):
    if row_index < size:
        i = row_index+1

        curr_st[row_index][col_index], curr_st[i][col_index] = curr_st[i][col_index], curr_st[row_index][col_index]
    return curr_st

def left(curr_st, row_index, col_index):
    if col_index > 0:
        j = col_index-1

        curr_st[row_index][col_index], curr_st[row_index][j] = curr_st[row_index][j], curr_st[row_index][col_index]
    return curr_st

def right(curr_st, row_index, col_index):
    if col_index < size:
        j = col_index+1

        curr_st[row_index][col_index], curr_st[row_index][j] = curr_st[row_index][j], curr_st[row_index][col_index]
    return curr_st

def compare(curr_st, goal_st):
    if curr_st == goal_st:
        return 1
    else:
        return 0

visited = []

def dfs(init_state, goal_st):
    global visited

    visited.append(init_state)
    curr_st = init_state
    i, j = get_empty_space(init_state)

    tcopy_st = copy.deepcopy(curr_st)
    tcopy_st = top(tcopy_st, i, j)
    if compare(tcopy_st, goal_st):
        print("found\n")
        disp(goal_st)
        return True

    elif curr_st != tcopy_st:
        if tcopy_st not in visited:
            if(dfs(tcopy_st, goal_st)):
                disp(tcopy_st)
                return True
            

    bcopy_st = copy.deepcopy(curr_st)
    bcopy_st = bottom(bcopy_st, i, j)
    if compare(bcopy_st, goal_st):
        print("found\n")
        disp(goal_st)
        return True
    elif curr_st != bcopy_st:
        if bcopy_st not in visited:
            if dfs(bcopy_st, goal_st):
                disp(bcopy_st)
                return True
        

    lcopy_st = copy.deepcopy(curr_st)
    lcopy_st = left(lcopy_st, i, j)
    if compare(lcopy_st, goal_st):
        print("found\n")
        disp(goal_st)
        return True
        
    elif curr_st != lcopy_st:
        if lcopy_st not in visited:
            if dfs(lcopy_st, goal_st):
                disp(lcopy_st)
                return True
        

    rcopy_st = copy.deepcopy(curr_st)
    rcopy_st = right(rcopy_st, i, j)
    if compare(rcopy_st, goal_st):
        print("found\n")
        disp(goal_st)
        return True
        
    elif curr_st != rcopy_st:
        if rcopy_st not in visited:
            if dfs(rcopy_st, goal_st):
                disp(rcopy_st)
                return True

    visited.pop()
    return False



def bfs(init_state, goal_st):
    global queue

    enqueue(init_state)
    while(len(queue) > 0):
        curr_st = dequeue()

        
        i, j = get_empty_space(curr_st)
        tcopy_st = copy.deepcopy(curr_st)
        tcopy_st = top(tcopy_st, i, j)
        if compare(tcopy_st, goal_st):
            print("found\n")
            break
        elif curr_st != tcopy_st:
            enqueue(tcopy_st)
            
        bcopy_st = copy.deepcopy(curr_st)
        bcopy_st = bottom(bcopy_st, i, j)
        if compare(bcopy_st, goal_st):
            print("found\n")
            break
        elif curr_st != bcopy_st:
            enqueue(bcopy_st)
            
        lcopy_st = copy.deepcopy(curr_st)
        lcopy_st = left(lcopy_st, i, j)
        if compare(lcopy_st, goal_st):
            print("found\n")
            break
        elif curr_st != lcopy_st:
            enqueue(lcopy_st)
            
        rcopy_st = copy.deepcopy(curr_st)
        rcopy_st = right(rcopy_st, i, j)
        if compare(rcopy_st, goal_st):
            print("found\n")
            break
        elif curr_st != rcopy_st:
            enqueue(rcopy_st)

    print("not found")



init_state = [[2, 0, 3], [1, 8, 4], [7, 6, 5]]
goal_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
# bfs(init_state, goal_state)
dfs(init_state, goal_state)


