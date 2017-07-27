import random

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in xrange(0, len(l), n):
        yield l[i:i + n]

file = raw_input("Enter dataset file name: ")
print "you entered", file

k = raw_input("Enter K: ")
print "you entered", k

'''file = 'teste.txt'
k = 5'''

dataset = open(file, 'r')
lines = dataset.readlines()

collum_numbers = lines[1]
line_number = len(lines) - (int(collum_numbers)+2)

#creating a random order
order = []
for i in range(int(collum_numbers)+3,len(lines)+1):
    order.append(i)
random.shuffle(order)

chunk_number = int(line_number/k)

folds = list(chunks(order, chunk_number))

test_groups = []
validadtion_groups = []
all_lines = order
for i in range(len(folds)):
    valid = all_lines[:]
    test = []
    for j in range(len(folds[i])):
        valid.remove(folds[i][j])
    test_groups.append(folds[i])
    validadtion_groups.append(valid)

print len(lines)
print validadtion_groups

#writing the files
for i in range(len(folds)):
    f = open(file+'_validation_'+str(i+1)+'.dat','w')
    t = open(file+'_test_'+str(i+1)+'.dat','w')
    for j in range(int(collum_numbers)+2):
        f.write(lines[j])
        t.write(lines[j])
    for l in range(len(test_groups[i])):
        if test_groups[i][l] == len(lines):
            t.write(lines[test_groups[i][l]-1]+'\n')
        else:
            t.write(lines[test_groups[i][l]-1])
    for m in range(len(validadtion_groups[i])):
        print validadtion_groups[i][m], len(lines)
        if validadtion_groups[i][m]== len(lines):

            f.write(lines[validadtion_groups[i][m]-1]+'\n')
        else:
            f.write(lines[validadtion_groups[i][m]-1])

f.close()
t.close()
