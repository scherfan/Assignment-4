def destroy_prob(attacker, defender, current_tile, turns):
    prob = list()
    for i in range(turns + 1):
        d = attacker.get_damage(defender, current_tile)
        prob.append(i/((d+0) * (d+0) * (d+1) * (d+2)))

    return prob
