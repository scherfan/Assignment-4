def destroy_prob(attacker, defender, current_tile, turns):
    prob = list()

    for i in range(turns + 1):
        d = attacker.get_damage(defender, current_tile) # get attacker damage
        prob.append(((d * 0.2) * i)/defender.health) # append probability at that turn to prob
        
        defender.health
    return prob

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
    print(memo)
    return memoized_f

@memoize
def prob(damage, health, turn):
    total_prob = 0
    
    if turn == 0 or health <= 0:
        return health <= 0

    for modifier in range(-1, 3):
        abs_modifier = abs(modifier)
        percent = (abs_modifier is 0) * 10 + 40/(2 ** abs_modifier)
        total_prob += percent * prob(damage, health - (damage + modifier), turn-1)

    return total_prob
