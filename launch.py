from itertools import combinations
spaceships = ["Bear1", "Bear2", "Orca1", "Moose1", "Bumblebee1", "Bumblebee2", "Bumblebee3", "Bumblebee4", "Orca2", "Moose2", "Bear3"]
arr_of_tuples = []
for ship in spaceships:
    if ship == "Orca1":
        for i in range (4,16): ##
            arr_of_tuples.append((ship, i))
    if ship == "Moose1":
        for i in range(5,7):
            arr_of_tuples.append((ship, i))
    if ship == "Bear2":
        for i in range(10,17): ##
            arr_of_tuples.append((ship, i))
    if ship == "Bumblebee1":
        for i in range(12,30):
            arr_of_tuples.append((ship, i))
    if ship == "Bumblebee2":
        for i in range(13,30):
            arr_of_tuples.append((ship, i))

#print(len(arr_of_tuples)) #number of tuples
            
def single_ship(single_comb):
    add = True
    for ship in spaceships:
        count = 0
        for j in single_comb:
            if j[0] == ship and count >= 1:
                add = False
                break
            elif j[0] == ship and count == 0:
                count += 1
        if add == False:
            break
    return add

def single_day(single_comb):
    add = True
    for i in range (2, 30):
        count = 0
        for j in single_comb:
            if j[1] == i and count >= 1:
                add = False
                break
            elif j[1] == i and count == 0:
                count += 1
        if add == False:
            break
    return add

def valid_comb(single_comb):
    constraint = []
    for i in range(len(single_comb)):
        if "Bear" in single_comb[i][0]:
            constraint.append(single_comb[i][1] + 1)
        if "Moose" in single_comb[i][0]:
            constraint.append(single_comb[i][1] - 1)
            constraint.append(single_comb[i][1] + 4)
            constraint.append(single_comb[i][1] + 3)
            constraint.append(single_comb[i][1] + 2)
            constraint.append(single_comb[i][1] + 1)
        if "Orca" in single_comb[i][0]:
            constraint.append(single_comb[i][1] - 1)
            constraint.append(single_comb[i][1] + 1)
        
    for i in range(len(single_comb)):
        if single_comb[i][1] in constraint:
            return False
    
    return True

comb = list(combinations(arr_of_tuples, 5))
tot = []
for i in range(len(comb)):
    if single_ship(comb[i]) and single_day(comb[i]) and valid_comb(comb[i]):
        tot.append(comb[i])

#print(len(tot))

spaceships = ["Bumblebee3", "Bumblebee4", "Orca2", "Moose2", "Bear3"]
second_arr_of_tuples = []
for ship in spaceships:
    if ship == "Bumblebee3":
        for i in range(14,30):
            second_arr_of_tuples.append((ship, i))
    if ship == "Bumblebee4":
        for i in range(15,30):
            second_arr_of_tuples.append((ship, i))
    if ship == "Orca2":
        for i in range(20,30):
            second_arr_of_tuples.append((ship, i))
    if ship == "Moose2":
        for i in range(23,25):
            second_arr_of_tuples.append((ship, i))

#print(len(second_arr_of_tuples))

comb = list(combinations(second_arr_of_tuples, 4))
second_tot = []
for i in range(len(comb)):
    if single_ship(comb[i]) and single_day(comb[i]) and valid_comb(comb[i]):
        second_tot.append(comb[i])

#print(len(second_tot))


dictionary = {}
for i in range(4, 16):
    dictionary[('Orca1', i)] = i - 3

dictionary[('Moose1', 5)] = 0
dictionary['Moose1', 6] = 7

start = 0
for i in range(10, 17): ##
    dictionary[('Bear2', i)] = start
    start += 2

start = 0
for i in range(12, 30):
    dictionary[('Bumblebee1', i)] = start
    start += 0.5

start = 0
for i in range(13, 30):
    dictionary[('Bumblebee2', i)] = start
    start += 0.5

start = 0
for i in range(14, 30):
    dictionary[('Bumblebee3', i)] = start
    start += 0.5

start = 0
for i in range(15, 30):
    dictionary[('Bumblebee4', i)] = start
    start += 0.5

start = 0
for i in range(20, 30):
    dictionary[('Orca2', i)] = start
    start += 1

start = 0
for i in range(23, 25):
    dictionary[('Moose2', i)] = start
    start += 7

#print(dictionary)

min = 1000
for i in range(len(tot)):
    curr = 0
    for j in range (len(tot[i])):
        curr += dictionary[tot[i][j]]
    if curr < min:
        min = curr

second_min = 1000
for i in range(len(second_tot)):
    curr = 0
    if second_tot[i][0][0] == "Bumblebee3" and second_tot[i][0][1] != 15:
        continue
    if second_tot[i][0][0] == "Bumblebee4" and second_tot[i][0][1] != 16:
        continue
    for j in range(len(second_tot[i])):
        curr += dictionary[second_tot[i][j]]
    if curr < second_min:
        second_min = curr
    if curr == 0:
        print(second_tot[i])
        break

#print(min)
#print(second_min)

minimum_val = 2 + min + second_min # 2 from the cost of delaying the Bear I launch

print(minimum_val)