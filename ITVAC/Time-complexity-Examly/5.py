T = int(input())

def num_z(n):
    z = 0
    j = 1
    while(n >= 5**j):
        z = z + int(n/(5**j))
        j = j + 1
    return(z)

for i in range(T):
    arr = []
    z = int(input())
    ub = 5 * z
    calc_z = num_z(ub)

    while((ub not in arr) and (z != calc_z)):
        arr.append(ub)
        if(calc_z > z):
            ub = ub - ((calc_z - z)*5)
        else:
            ub = ub + ((z - calc_z)*5)
        calc_z = num_z(ub)


    if(z == calc_z):
        print('5')
        print(ub, ub+1, ub+2, ub+3, ub+4)
    else:
        print('0')
