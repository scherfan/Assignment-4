def destroy_prob(attacker, defender, current_tile, turns):
    prob = list()

    for i in range(turns + 1):
        d = attacker.get_damage(defender, current_tile) # get attacker damage
        prob.append(((d * 0.2) * i)/defender.health) # append probability at that turn to prob
        
        defender.health
    return prob

def probability(damage, health, turn):
    """
compute the probability of destroying

damage - defender.health
"""
    total_chance = 0
    for i in range(-1, 3):
        if i == -1 or i == 1:
            pchance = 0.2
        elif i == 0:
            pchance = 0.5
        else:
            pchance = 0.1

        if damage + i >= defender.health:
            total_chance += pchance
    return 
