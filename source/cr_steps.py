from decimal import Decimal, ROUND_HALF_UP
import math

def hit_dice_type(window, size):
    parts = window.label_con_addition.cget("text").split(" ", maxsplit=1)
    hit_dice = parts[0] if len(parts) > 0 else "d4"
    hp_modifier = parts[1] if len(parts) > 1 else "+ 0"
    match size:
        case "Tiny":
            hit_dice = "d4"
        case "Small":
            hit_dice = "d6"
        case "Medium":
            hit_dice = "d8"
        case "Large":
            hit_dice = "d10"
        case "Huge":
            hit_dice = "d12"
        case "Gargantuan":
            hit_dice = "d20"
        case _:
            hit_dice = "d4"
    window.label_con_addition.configure(text = f"{hit_dice} {hp_modifier}")

def int_check(value):
    if value is None or value == "":
        return 0
    else:
        try:
            return int(value)
        except ValueError:
            return 0

def hp_modifier(window, con_modifier, hit_dice_amount):
    con_modifier = int_check(con_modifier)
    hit_dice_amount = int_check(hit_dice_amount)
    parts = window.label_con_addition.cget("text").split()
    hit_dice_type = parts[0] if len(parts) > 0 else "d4"
    final_modifier = con_modifier * hit_dice_amount
    if final_modifier >= 0:
        operation = "+"
    else:
        final_modifier *= -1
        operation = "-"
    window.label_con_addition.configure(text = f"{hit_dice_type} {operation} {final_modifier}")

def average_hp(window, hit_dice_amount):
    hit_dice_amount = int_check(hit_dice_amount)
    parts = window.label_con_addition.cget("text").split()
    hit_dice_type = parts[0] if len(parts) > 0 else "d4"
    operation = parts[1] if len(parts) > 1 else "+"
    try:
        hp_modifier = int(parts[2]) if len(parts) > 2 else 0
    except ValueError:
        hp_modifier = 0
    match hit_dice_type:
        case "d4":
            hit_dice_hp = 2.5
        case "d6":
            hit_dice_hp = 3.5
        case "d8":
            hit_dice_hp = 4.5
        case "d10":
            hit_dice_hp = 5.5
        case "d12":
            hit_dice_hp = 6.5
        case "d20":
            hit_dice_hp = 10.5
        case _:
            hit_dice_hp = 2.5
    if operation == "+":
        average_hp = hit_dice_amount * hit_dice_hp + hp_modifier
    else:
        average_hp = hit_dice_amount * hit_dice_hp - hp_modifier
    window.label_hp_result.configure(text = f"{math.floor(average_hp)}")

def average_damage(window, damage_1, damage_2, damage_3):
    damage_1 = int_check(damage_1)
    damage_2 = int_check(damage_2)
    damage_3 = int_check(damage_3)
    average_damage = (damage_1 + damage_2 + damage_3) / 3
    window.label_damage_result.configure(text = f"{math.floor(average_damage)}")

def decrement_cr(cr):
    cr_levels = [0, 0.125, 0.25, 0.5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    idx = cr_levels.index(cr)
    return cr_levels[max(idx - 1, len(cr_levels) - len(cr_levels))]

def increment_cr(cr):
    cr_levels = [0, 0.125, 0.25, 0.5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    idx = cr_levels.index(cr)
    return cr_levels[min(idx + 1, len(cr_levels) - 1)]

def cr_adjustment(base_cr, stat_diff):
    cr = base_cr
    if stat_diff > 1:
        while stat_diff > 1:
            stat_diff -= 2
            cr = decrement_cr(cr)
    elif stat_diff < -1:
        while stat_diff < -1:
            stat_diff += 2
            cr = increment_cr(cr)
    return cr

def cr_calculation(window, ac, hp, ab_or_sdc, dpr):
    hp_tiers = (
        (float("-inf"), 6, 0, 13),
        (7, 35, 0.125, 13),
        (36, 49, 0.25, 13),
        (50, 70, 0.5, 13),
        (71, 85, 1, 13),
        (86, 100, 2, 13),
        (101, 115, 3, 13),
        (116, 130, 4, 14),
        (131, 145, 5, 15),
        (146, 160, 6, 15),
        (161, 175, 7, 15),
        (176, 190, 8, 16),
        (191, 205, 9, 16),
        (206, 220, 10, 17),
        (221, 235, 11, 17),
        (236, 250, 12, 17),
        (251, 265, 13, 18),
        (266, 280, 14, 18),
        (281, 295, 15, 18),
        (296, 310, 16, 18),
        (311, 325, 17, 19),
        (326, 340, 18, 19),
        (341, 355, 19, 19),
        (356, 400, 20, 19),
        (401, 445, 21, 19),
        (446, 490, 22, 19),
        (491, 535, 23, 19),
        (536, 580, 24, 19),
        (581, 625, 25, 19),
        (626, 670, 26, 19),
        (671, 715, 27, 19),
        (716, 760, 28, 19),
        (761, 805, 29, 19),
        (806, float("inf"), 30, 19)
    )
    for hp_stats in hp_tiers:
        if hp >= hp_stats[0] and hp <= hp_stats[1]:
            defensive_cr = cr_adjustment(hp_stats[2], hp_stats[3] - ac)
            break
    dpr_tiers = (
        (float("-inf"), 1, 0, 3, 13),
        (2, 3, 0.125, 3, 13),
        (4, 5, 0.25, 3, 13),
        (6, 8, 0.5, 3, 13),
        (9, 14, 1, 3, 13),
        (15, 20, 2, 3, 13),
        (21, 26, 3, 4, 13),
        (27, 32, 4, 5, 14),
        (33, 38, 5, 6, 15),
        (39, 44, 6, 6, 15),
        (45, 50, 7, 6, 15),
        (51, 56, 8, 7, 16),
        (57, 62, 9, 7, 16),
        (63, 68, 10, 7, 16),
        (69, 74, 11, 8, 17),
        (75, 80, 12, 8, 17),
        (81, 86, 13, 8, 18),
        (87, 92, 14, 8, 18),
        (93, 98, 15, 8, 18),
        (99, 104, 16, 9, 18),
        (105, 110, 17, 10, 19),
        (111, 116, 18, 10, 19),
        (117, 122, 19, 10, 19),
        (123, 140, 20, 10, 19),
        (141, 158, 21, 11, 20),
        (159, 176, 22, 11, 20),
        (177, 194, 23, 11, 20),
        (195, 212, 24, 12, 21),
        (213, 230, 25, 12, 21),
        (231, 248, 26, 12, 21),
        (249, 266, 27, 13, 22),
        (267, 284, 28, 13, 22),
        (285, 302, 29, 13, 22),
        (303, float("inf"), 30, 14, 23)
    )
    for dpr_stats in dpr_tiers:
        if dpr >= dpr_stats[0] and dpr <= dpr_stats[1]:
            if window.offence_type.get() == "ab":
                offensive_cr = cr_adjustment(dpr_stats[2], dpr_stats[3] - ab_or_sdc)
                break
            elif window.offence_type.get() == "sdc":
                offensive_cr = cr_adjustment(dpr_stats[2], dpr_stats[4] - ab_or_sdc)
                break
    average_cr = (defensive_cr + offensive_cr) / 2
    if average_cr >= 0 and average_cr <= 0.125:
        low = average_cr - 0
        high = 0.125 - average_cr
        if low < high:
            final_cr = 0
        else:
            final_cr = 0.125
    elif average_cr >= 0.125 and average_cr <= 0.25:
        low = average_cr - 0.125
        high = 0.25 - average_cr
        if low < high:
            final_cr = 0.125
        else:
            final_cr = 0.25
    elif average_cr >= 0.25 and average_cr <= 0.5:
        low = average_cr - 0.25
        high = 0.5 - average_cr
        if low < high:
            final_cr = 0.25
        else:
            final_cr = 0.5
    elif average_cr >= 0.5 and average_cr <= 1:
        low = average_cr - 0.5
        high = 1 - average_cr
        if low < high:
            final_cr = 0.5
        else:
            final_cr = 1
    else:
        average_cr = Decimal(f"{average_cr}")
        final_cr = average_cr.quantize(Decimal("1"), rounding = ROUND_HALF_UP)
    return final_cr

def resistances_immunities_and_vulnerabilities(hp, cr, resist_or_immune, immune_check, vulnerable):
    if resist_or_immune == "yes":
        if immune_check == "resistance":
            if cr <= 4:
                hp *= 2
            elif cr >= 5 and cr <= 10:
                hp *= 1.5
            elif cr >= 11 and cr <= 16:
                hp *= 1.25
        elif immune_check == "immunity":
            if cr <= 10:
                hp *= 2
            elif cr >= 11 and cr <= 16:
                hp *= 1.5
            elif cr >= 17:
                hp *= 1.25
    if vulnerable == "yes":
        hp //= 2
    return math.floor(hp)

def features(window, ac, hp, effective_hp, ab_or_sdc, dpr, cr, feature):
    match feature:
        case "Aggressive":
            dpr += 2
        case "Ambusher" | "Pack Tactics":
            if window.offence_type.get() == "ab":
                ab_or_sdc += 1
        case "Avoidance" | "Constrict" | "Parry" | "Stench" | "Web":
            ac += 1
        case "Blood Frenzy":
            if window.offence_type.get() == "ab":
                ab_or_sdc += 4
        case "Damage Transfer":
            effective_hp *= 2
            dpr += hp / 3
        case "Frightful Presence" | "Horrifying Visage":
            if cr <= 10:
                effective_hp *= 1.25
        case "Legendary Resistance":
            amount = int_check(window.entry_features[9].get())
            if cr <= 4:
                effective_hp += 10 * amount
            elif cr >= 5 and cr <= 10:
                effective_hp += 20 * amount
            elif cr >= 11:
                effective_hp += 30 * amount
        case "Magic Resistance" | "Superior Invisibility":
            ac += 2
        case "Nimble Escape":
            ac += 4
            if window.offence_type.get() == "ab":
                ab_or_sdc += 4
        case "Possession":
            effective_hp *= 2
        case "Regeneration":
            amount = int_check(window.entry_features[16].get())
            effective_hp += 3 * amount
        case "Relentless" | "Undead Fortitude":
            if cr <= 4:
                effective_hp += 7
            elif cr >= 5 and cr <= 10:
                effective_hp += 14
            elif cr >= 11 and cr <= 16:
                effective_hp += 21
            elif cr >= 17:
                effective_hp += 28
        case "Shadow Stealth":
            ac += 4
    return ac, math.floor(effective_hp), ab_or_sdc, math.floor(dpr)

def flying_speed(ac, cr):
    if cr <= 10:
        ac += 2
    return ac

def saving_throw_bonuses(ac, save):
    match save:
        case "3-4":
            ac += 2
        case "5+":
            ac += 4
    return ac

def score_calculation(window, con_mod, ab_or_sdc_mod, pb):
    con_score = con_mod * 2 + 10
    con_scores = f"{con_score}-{con_score + 1}"
    cha_scores = "N/A"
    wis_scores = "N/A"
    if window.offence_type.get() == "ab":
        attack_score = (ab_or_sdc_mod - pb) * 2 + 10
        attack_scores = f"{attack_score}-{attack_score + 1}"
    elif window.offence_type.get() == "sdc":
        attack_score = (ab_or_sdc_mod - pb - 8) * 2 + 10
        attack_scores = f"{attack_score}-{attack_score + 1}"
    if window.feature_types[6].get() == "Fiendish Blessing":
        cha_mod = window.entry_features[6].get()
        if cha_mod is None or cha_mod == "":
            cha_mod = "N/A"
        else:
            try:
                cha_mod = int(cha_mod)
            except ValueError:
                cha_mod = "N/A"
        if cha_mod != "N/A":
            cha_score = cha_mod * 2 + 10
            cha_scores = f"{cha_score}-{cha_score + 1}"
    if window.feature_types[15].get() == "Psychic Defence":
        wis_mod = window.entry_features[15].get()
        if wis_mod is None or wis_mod == "":
            wis_mod = "N/A"
        else:
            try:
                wis_mod = int(wis_mod)
            except ValueError:
                wis_mod = "N/A"
        if wis_mod != "N/A":
            wis_score = wis_mod * 2 + 10
            wis_scores = f"{wis_score}-{wis_score + 1}"
    return con_scores, attack_scores, cha_scores, wis_scores

def final_results(window, ac, effective_ac, hp, effective_hp, ab_or_sdc, effective_ab_or_sdc, dpr, effective_dpr, resist_or_immune, immune_check, vulnerable, feature_list, flying, save, con_mod, repeat = 0):
    ac = int_check(ac)
    effective_ac = int_check(effective_ac)
    hp = int_check(hp)
    effective_hp = int_check(effective_hp)
    ab_or_sdc = int_check(ab_or_sdc)
    effective_ab_or_sdc = int_check(effective_ab_or_sdc)
    dpr = int_check(dpr)
    effective_dpr = int_check(effective_dpr)
    con_mod = int_check(con_mod)
    new_effective_ac = ac
    new_effective_hp = hp
    new_effective_ab_or_sdc = ab_or_sdc
    new_effective_dpr = dpr
    cr = cr_calculation(window, effective_ac, effective_hp, effective_ab_or_sdc, effective_dpr)
    if resist_or_immune == "yes" or vulnerable == "yes":
        new_effective_hp = resistances_immunities_and_vulnerabilities(new_effective_hp, cr, resist_or_immune, immune_check, vulnerable)
    for feature_var in feature_list:
        feature = feature_var.get()
        if feature != "":
            new_effective_ac, new_effective_hp, new_effective_ab_or_sdc, new_effective_dpr = features(window, new_effective_ac, hp, new_effective_hp, new_effective_ab_or_sdc, new_effective_dpr, cr, feature)
    if flying == "yes":
        new_effective_ac = flying_speed(new_effective_ac, cr)
    if save == "3-4" or save == "5+":
        new_effective_ac = saving_throw_bonuses(new_effective_ac, save)
    new_cr = cr_calculation(window, new_effective_ac, new_effective_hp, new_effective_ab_or_sdc, new_effective_dpr)
    if new_cr != cr:
        repeat += 1
        if repeat >= 10:
            if new_cr < cr:
                new_effective_ac = effective_ac
                new_effective_hp = effective_hp
                new_effective_ab_or_sdc = effective_ab_or_sdc
                new_effective_dpr = effective_dpr
                new_cr = cr
        else:
            return final_results(window, ac, new_effective_ac, hp, new_effective_hp, ab_or_sdc, new_effective_ab_or_sdc, dpr, new_effective_dpr, resist_or_immune, immune_check, vulnerable, feature_list, flying, save, con_mod, repeat)
    window.label_effective_ac_result.configure(text = f"{int(new_effective_ac)}")
    window.label_effective_hp_result.configure(text = f"{int(new_effective_hp)}")
    window.label_effective_ab_or_sdc_result.configure(text = f"{int(new_effective_ab_or_sdc)}")
    window.label_effective_damage_result.configure(text = f"{int(new_effective_dpr)}")
    if new_cr <= 4:
        pb = 2
    elif new_cr >= 5 and new_cr <= 8:
        pb = 3
    elif new_cr >= 9 and new_cr <= 12:
        pb = 4
    elif new_cr >= 13 and new_cr <= 16:
        pb = 5
    elif new_cr >= 17 and new_cr <= 20:
        pb = 6
    elif new_cr >= 21 and new_cr <= 24:
        pb = 7
    elif new_cr >= 25 and new_cr <= 28:
        pb = 8
    elif new_cr >= 29 and new_cr <= 30:
        pb = 9
    window.label_proficiency_bonus_result.configure(text = f"+{int(pb)}")
    match new_cr:
        case 0.125:
            new_cr = "1/8"
        case 0.25:
            new_cr = "1/4"
        case 0.5:
            new_cr = "1/2"
    window.label_final_cr_result.configure(text = f"{new_cr}")
    con_scores, attack_scores, cha_scores, wis_scores = score_calculation(window, con_mod, ab_or_sdc, pb)
    window.label_possible_con_result.configure(text = f"{con_scores}")
    window.label_possible_attack_stat_result.configure(text = f"{attack_scores}")
    window.label_possible_cha_result.configure(text = f"{cha_scores}")
    window.label_possible_wis_result.configure(text = f"{wis_scores}")

def reset_window(window):
    window.label_con_addition.configure(text = "d4 + 0")
    window.label_hp_result.configure(text = "0")
    window.label_damage_result.configure(text = "0")
    window.label_effective_ac_result.configure(text = "0")
    window.label_effective_hp_result.configure(text = "0")
    window.label_effective_ab_or_sdc_result.configure(text = "0")
    window.label_effective_damage_result.configure(text = "0")
    window.label_proficiency_bonus_result.configure(text = "+2")
    window.label_final_cr_result.configure(text = "0")
    window.label_possible_con_result.configure(text = "0")
    window.label_possible_attack_stat_result.configure(text = "0")
    window.label_possible_cha_result.configure(text = "0")
    window.label_possible_wis_result.configure(text = "0")
    window.entry_ac.delete(0, 'end')
    window.entry_con_modifier.delete(0, 'end')
    window.entry_hit_dice.delete(0, 'end')
    window.entry_ab_or_sdc.delete(0, 'end')
    window.entry_round_1.delete(0, 'end')
    window.entry_round_2.delete(0, 'end')
    window.entry_round_3.delete(0, 'end')
    window.combobox_size.set('')
    window.combobox_save_bonuses.set('')
    window.checkbutton_ab_or_sdc.deselect()
    window.checkbutton_resistance_or_immunity.deselect()
    window.checkbutton_immunity_check.deselect()
    window.checkbutton_vulnerability_check.deselect()
    window.checkbutton_fly_and_range.deselect()
    for check in window.checkbutton_features:
        check.deselect()
    for entry in window.entry_features:
        if entry is not None:
            entry.delete(0, 'end')
