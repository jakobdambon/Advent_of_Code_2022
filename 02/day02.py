# read in data
with open('02/input.txt', 'r') as file:
    data = file.read()

x = [i.split(' ') for i in data.split("\n")]
# first part
def score_fun(x, y):
    # matrix for points
    result = [
        [3, 6, 0],
        [0, 3, 6],
        [6, 0, 3]
    ]
    # dictionaries for indices
    dict_x = {
        "A": 0,
        "B": 1, 
        "C": 2
    }
    dict_y = {
        "X": 0,
        "Y": 1, 
        "Z": 2
    }
    # total score as points of result plus my choice
    score = result[dict_x[x]][dict_y[y]] + dict_y[y] + 1
    return score

points = [score_fun(r[0], r[1]) for r in x[:-1]]
print(sum(points))

# second part

def score_fun2(x, y):
    result = [
        [3, 6, 0],
        [0, 3, 6],
        [6, 0, 3]
    ]
    dict_x = {
        "A": 0,
        "B": 1, 
        "C": 2
    }
    dict_result = {
        "X": 0,
        "Y": 3, 
        "Z": 6
    }
    # this gets index and therefore my choice
    y_choice = result[dict_x[x]].index(dict_result[y])
    score = result[dict_x[x]][y_choice] + y_choice + 1
    return score

points2 = [score_fun2(r[0], r[1]) for r in x[:-1]]
print(sum(points2))
