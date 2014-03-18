def destroy_prob(attacker_d, defender_hp, turns):
    prob_list = list()

    for turn in range(turns + 1):
        #d = attacker.get_damage(defender_hp, current_tile) # get attacker damage
        prob_list.append(memo_prob(attacker_d, defender_hp, turn, {})) # append probability at that turn to prob
        
    return prob_list

def memo_prob(damage, health, turn, memo2 = {}):

    if (health, turn) in memo2:
        return memo2[(health, turn)]
    
    total_prob = 0
    
    if turn == 0 or health <= 0:
        return health <= 0

    for modifier in range(-1, 3):
        if modifier is -1 or modifier is 1:
            percent = 0.2
        elif modifier is 0:
            percent = 0.5
        elif modifier is 2:
            percent = 0.1
            
        #abs_modifier = abs(modifier)
        #percent = (abs_modifier is 0) * 0.1 + 0.4/(2 ** abs_modifier)
        total_prob += percent * memo_prob(damage, health - (damage + modifier), turn-1, memo2)

    memo2[(health, turn)] = total_prob
    #print(memo2)
    return memo2[(health, turn)]

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
        percent = (abs_modifier is 0) * 0.1 + 0.4/(2 ** abs_modifier)
        total_prob += percent * prob(damage, health - (damage + modifier), turn-1)

    return total_prob


print(destroy_prob(4, 15, 5))
print(destroy_prob(3, 15, 6))
print(destroy_prob(0, 15, 9))

print(memo_prob(3, 12, 3))
print(prob(3, 12, 3))

#print(memo_prob(1, 100, 100))
#print(prob(2, 100, 30))

"""
for modifier in range(-1, 3):
abs_modifier = abs(modifier)
percent = (abs_modifier is 0) * 10 + 40/(2 ** abs_modifier)
print(percent)


def stupid(x):
print(((40/3) * (x ** 3)) - 30 * (x ** 2) - (40/3) * x  + 50)

stupid3(-1)
stupid(0)
stupid(1)
stupid(2)

def stupid2(x):
x = abs(x)
print(10 * (x ** 2) - 40 * x +50)

stupid2(-1)
stupid2(0)
stupid2(1)
stupid2(2)


"""
