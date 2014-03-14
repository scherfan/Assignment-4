"""
def destroy_prob(attacker, defender, current_tile, turns):
    prob = list()

    for i in range(turns + 1):
        d = attacker.get_damage(defender, current_tile) # get attacker damage
         # append probability at that turn to prob
        prob.append(((d * 0.2) * i)/defender.health)
        
    return prob
"""
def destroy_prob(attacker, defender, current_tile, turns):
    prob = list()
    memo = dict()
    for i in range(turns + 1):    
        if defender.health < attacker.get_damage(defender, current_tile):
            prob.append(1)
        else:
            prob.append(0.1)
        
    return prob
