def memoize(f):
    """
    Takes a function and spits out a memoized version of that function
    """

    memo = {}
    def memoized_f(*args):
        if args in memo:
            return memo[args]
        memo[args] = f(*args)
        return memo[args]
    return memoized_f

@memoize
def prob(damage, health, turn):
    total_prob = 0

    if turn == 0 or health <= 0:
        return health <= 0

    for modifier in range(-1, 3):
        abs_modifier = abs(modifier)
        percent = (abs_modifier is 0) * 0.1 + 0.4/(2 ** abs_modifier) # a fun way 
        total_prob += percent * prob(damage, health - (damage + modifier), turn-1)

    return total_prob
"""
print(prob(5, 12, 2))
print(prob(3, 12, 3))

print(prob(1, 100, 10))
print(prob(2, 100, 30))
"""
