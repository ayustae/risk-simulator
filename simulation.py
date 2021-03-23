#!/usr/bin/env python3
# coding=utf-8

#------------------------------------#
# Import the uniform distribution
#------------------------------------#
from random import uniform

#------------------------------------#
# Import the square root function
#------------------------------------#
from math import sqrt

#------------------------------------#
# Define dice_roll function
#------------------------------------#
def dice_roll(sides: int):
    """
    Calculate a dice roll of a given number of sides.
    Expects an integer.
    """
    return int(uniform(1,sides + 1))

#------------------------------------#
# Define battle function
#------------------------------------#
def battle(attacker, defender):
    """
    This function simulates a battle between two armies.
    """
    # Count the nomber of rounds
    rounds = 0
    # The battle continues until one army is defeated
    while True:
        rounds += 1
        ### ARTILLERY PHASE ###
        # Attacker damage
        arty_dmg_att = 0
        for i in range(0, 2*attacker.get_artillery()):
            if dice_roll(6) > 2:
                arty_dmg_att += 1
        # Defender damage
        arty_dmg_def = 0
        for i in range(0, 2*defender.get_artillery()):
            if dice_roll(6) > 2:
                arty_dmg_def += 1
        # Absorb artillery damage
        attacker.absorb_damage(arty_dmg_def)
        defender.absorb_damage(arty_dmg_att)
        # Check if there is a winner
        if not attacker.is_alive() or not defender.is_alive():
            break
        ### ARCHERY PHASE ###
        # Attacker damage
        arch_dmg_att = 0
        for i in range(0, attacker.get_archery()):
            if dice_roll(6) > 4:
                arch_dmg_att += 1
        # Defender damage
        arch_dmg_def = 0
        for i in range(0, defender.get_archery()):
            if dice_roll(6) > 4:
                arch_dmg_def += 1
        # Absorb archery damage
        attacker.absorb_damage(arch_dmg_def)
        defender.absorb_damage(arch_dmg_att)
        # Check if there is a winner
        if not attacker.is_alive() or not defender.is_alive():
            break
        ### CAVALRY PHASE ###
        # Attacker damage
        cav_dmg_att = 0
        for i in range(0, attacker.get_cavalry()):
            if dice_roll(6) > 2:
                cav_dmg_att += 1
        # Defender damage
        cav_dmg_def = 0
        for i in range(0, defender.get_cavalry()):
            if dice_roll(6) > 2:
                cav_dmg_def += 1
        # Absorb cavalry damage
        attacker.absorb_damage(cav_dmg_def)
        defender.absorb_damage(cav_dmg_att)
        # Check if there is a winner
        if not attacker.is_alive() or not defender.is_alive():
            break
        ### INFANTRY PHASE ###
        # Attacker rolls
        rolls_att = []
        for i in range(0, min(attacker.get_total_size(), 3)):
            rolls_att.append(dice_roll(6))
        rolls_att.sort()    # Sort the list of rolls
        # Defender rolla
        rolls_def = []
        for i in range(0, min(defender.get_total_size(), 2)):
            rolls_def.append(dice_roll(6))
        rolls_def.sort()    # Sort the list of rolls
        # Get damage
        inf_dmg_att = 0
        inf_dmg_def = 0
        ## First comparison
        if len(rolls_att) > 0 and len(rolls_def) > 0:
            if rolls_att.pop(-1) > rolls_def.pop(-1):
                inf_dmg_att += 1
            else:
                inf_dmg_def += 1
        ## Second comparison
        if len(rolls_att) > 0 and len(rolls_def) > 0:
            if rolls_att.pop(-1) > rolls_def.pop(-1):
                inf_dmg_att += 1
            else:
                inf_dmg_def += 1
        # Absorb infantry damage
        attacker.absorb_damage(inf_dmg_def)
        defender.absorb_damage(inf_dmg_att)
        # Check if there is a winner
        if not attacker.is_alive() or not defender.is_alive():
            break
    # Return the total number of rounds and the winner
    if attacker.is_alive():
        return rounds, 'a'
    elif defender.is_alive():
        return rounds, 'd'
    else:
        raise Exception('Something bad happened in a battle') # DEBUG

#------------------------------------#
# Define simulation function
#------------------------------------#
def simulation(n_simulations, attacker, defender):
    # Variables used for statistics
    attacker_wins = 0.0
    defender_wins = 0.0
    rounds_list = []
    # Simulations
    for b in range(0,n_simulations):
        rounds,winner = battle(attacker.copy(), defender.copy())
        rounds_list.append(rounds)
        if winner == 'a':
            attacker_wins += 1
        elif winner == 'd':
            defender_wins += 1
        else:
            raise Exception('Something bad happened in the simulation') #DEBUG
    att_win_frac = attacker_wins/n_simulations
    def_win_frac = defender_wins/n_simulations
    rounds_avg = sum(rounds_list)/n_simulations
    rounds_std = sqrt(sum([(i-rounds_avg)**2 for i in rounds_list])/(n_simulations - 1))
    return {
            'attacker_win_fraction': att_win_frac,
            'defender_win_fraction': def_win_frac,
            'rounds_avg': rounds_avg,
            'rounds_std': rounds_std,
            }
