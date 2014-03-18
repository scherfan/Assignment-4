def destroy_prob(attacker, defender, current_tile, turns):
    prob_list = list()
    memo = {}

    if attacker.phony_damage == True:
        d = attacker.get_false_damage(defender, current_tile) # get falsified attacker damage
    else:
        d = attacker.get_damage(defender, current_tile) # get attacker damage
    for turn in range(turns + 1):
        prob_list.append(memo_prob(d, defender.health, turn, memo)) # append probability at that turn to prob
        
    return prob_list

def memo_prob(damage, health, turn, memo = {}):

    if (health, turn) in memo:
        return memo[(health, turn)]
    
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
            
        total_prob += percent * memo_prob(damage, health - (damage + modifier), turn-1, memo)

    memo[(health, turn)] = total_prob
    return memo[(health, turn)]
