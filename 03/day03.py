# read in data
with open('03/input.txt', 'r') as file:
    data = file.read()
# into list
x = [i.split(' ')[0] for i in data.split("\n")]

def get_match(x):
    # half length of string
    lh = int(len(x)/2)
    # split
    x0 = x[:lh]
    x0 = set([*x0])
    x1 = x[lh:]
    x1 = set([*x1])
    sect = list(x0.intersection(x1))
    return sect[0]

def get_value(x):
    # ASCII code
    ac = ord(x)
    # capital
    if (x.isupper()):
        val = ac-64+26
    else:
        val = ac-96
    
    return val

# first part
x_match = [get_match(s) for s in x[:-1]]
x_prio = [get_value(v) for v in x_match]
print(sum(x_prio))


# second part
def get_group(x):
    sect = list(set(x[0]).intersection(set(x[1])).intersection(set(x[2])))
    return sect[0]

# number of elves
l_x = int(len(x[:-1]))
# grouping and finding common item
x_group = [get_group(x[int(3*i):int(3*i+3)]) for i in range(int(l_x/3))]
x_gp_prio = [get_value(v) for v in x_group]
print(sum(x_gp_prio))