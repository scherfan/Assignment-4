def destroy_prob(attacker, defender, current_tile, turns):
    prob = list()


    for i in range(turns + 1):
        d = attacker.get_damage(defender, current_tile) # get attacker damage
        prob.append(((d * 0.2) * i)/defender.health) # append probability at that turn to prob
        

    return prob

