def destroy_prob(attacker, defender, current_tile, turns):
    prob = list()
    prob[turns] = d
    d = attacker.get_damage(defender, current_tile)
    return prob[turns]
