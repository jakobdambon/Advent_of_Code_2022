# read in data
with open('04/input.txt', 'r') as file:
    data = file.read()
# into list of 4 values
x = [i.replace("-", ",").split(',') for i in data.split("\n")]

# first part
def check_within(x):
    # transform into int
    y = [int(xx) for xx in x]
    if (
        # one within the other or vice versa
        ((y[0]>= y[2]) & (y[1]<= y[3])) | ((y[2]>= y[0]) & (y[3]<= y[1]))
    ):
        out = 1
    else:
        out = 0

    return out

check = [check_within(xx) for xx in x[:-1]]
print(sum(check))

# second part
def check_overlap(x):
    # transform into int
    y = [int(xx) for xx in x]
    if (
        # one boundary within two others
        ((y[0]>= y[2]) & (y[0]<= y[3])) | ((y[2]>= y[0]) & (y[2]<= y[1]))
    ):
        out = 1
    else:
        out = 0

    return out

check = [check_overlap(xx) for xx in x[:-1]]
print(sum(check))