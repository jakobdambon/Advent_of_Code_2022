# read in data
with open('01/input.txt', 'r') as file:
    data = file.read()
# change into list of integers (dropping last entry due to "")
x = [list(map(int, i.split('\n'))) for i in data.split("\n\n")[:-1]]
sum_x = [sum(l) for l in x]
# first answer
print(max(sum_x))
# second answer
sum_x.sort(reverse=True)
print(sum(sum_x[:3]))