def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if (2 * chickens + 4 * rabbits) == numlegs:
            return chickens, rabbits
    return None
numheads = 35
numlegs = 94
solution = solve(numheads, numlegs)

if solution:
    chickens, rabbits = solution
    print("Number of chickens:", chickens)
    print("Number of rabbits:", rabbits)
else:
    print("No solution found.")