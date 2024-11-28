def ways(stairs):
    if stairs<0:
        return 0
    if stairs == 0:
        return 1
    twostep = 0
    onestep=0
    if stairs>=2:
        twostep=ways(stairs-2)
    onestep=ways(stairs-1)
    return twostep+onestep
stairs = int(input("Enter the number of steps: "))
print("ways to climb stairs are", ways(stairs))