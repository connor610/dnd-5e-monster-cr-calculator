from decimal import Decimal, ROUND_HALF_UP

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

def hp_modifier(window, con_modifier, hit_dice_amount):
    if con_modifier is None or con_modifier == "":
        con_modifier = 0
    else:
        try:
            con_modifier = int(con_modifier)
        except ValueError:
            con_modifier = 0
    if hit_dice_amount is None or hit_dice_amount == "":
        hit_dice_amount = 0
    else:
        try:
            hit_dice_amount = int(hit_dice_amount)
        except ValueError:
            hit_dice_amount = 0
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
    if hit_dice_amount is None or hit_dice_amount == "":
        hit_dice_amount = 0
    else:
        try:
            hit_dice_amount = int(hit_dice_amount)
        except ValueError:
            hit_dice_amount = 0
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
    window.label_hp_result.configure(text = f"{int(average_hp // 1)}")

def average_damage(window, damage_1, damage_2, damage_3):
    if damage_1 is None or damage_1 == "":
        damage_1 = 0
    else:
        try:
            damage_1 = int(damage_1)
        except ValueError:
            damage_1 = 0
    if damage_2 is None or damage_2 == "":
        damage_2 = 0
    else:
        try:
            damage_2 = int(damage_2)
        except ValueError:
            damage_2 = 0
    if damage_3 is None or damage_3 == "":
        damage_3 = 0
    else:
        try:
            damage_3 = int(damage_3)
        except ValueError:
            damage_3 = 0
    average_damage = (damage_1 + damage_2 + damage_3) // 3
    window.label_damage_result.configure(text = f"{int(average_damage)}")

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

def resistances_immunities_and_vulnerabilities(window, ac, hp, effective_hp, ab_or_sdc, dpr, cr, resist_or_immune, immune_check, vulnerable, repeat = 0):
    new_effective_hp = hp
    if resist_or_immune == "yes":
        if immune_check == "resistance":
            if cr <= 4:
                new_effective_hp *= 2
            elif cr >= 5 and cr <= 10:
                new_effective_hp *= 1.5
            elif cr >= 11 and cr <= 16:
                new_effective_hp *= 1.25
        elif immune_check == "immunity":
            if cr <= 10:
                new_effective_hp *= 2
            elif cr >= 11 and cr <= 16:
                new_effective_hp *= 1.5
            elif cr >= 17:
                new_effective_hp *= 1.25
    if vulnerable == "yes":
        new_effective_hp //= 2
    new_cr = cr_calculation(window, ac, (new_effective_hp // 1), ab_or_sdc, dpr)
    if new_cr != cr:
        repeat += 1
        if repeat >= 10:
            if new_cr >= cr:
                return new_effective_hp // 1, new_cr
            else:
                return effective_hp // 1, cr
        else:
            return resistances_immunities_and_vulnerabilities(window, ac, hp, new_effective_hp, ab_or_sdc, dpr, new_cr, resist_or_immune, immune_check, vulnerable, repeat)
    return new_effective_hp // 1, new_cr

def features(window, ac, hp, effective_hp, ab_or_sdc, dpr, cr, feature, repeat = 0):
    effective_ac = ac
    new_effective_hp = hp
    effective_ab_or_sdc = ab_or_sdc
    effective_dpr = dpr
    match feature:
        case "Aggressive":
            effective_dpr += 2
        case "Ambusher" | "Pack Tactics":
            if window.offence_type.get() == "ab":
                effective_ab_or_sdc += 1
        case "Avoidance" | "Constrict" | "Parry" | "Stench" | "Web":
            effective_ac += 1
        case "Blood Frenzy":
            if window.offence_type.get() == "ab":
                effective_ab_or_sdc += 4
        case "Damage Transfer":
            new_effective_hp *= 2
            effective_dpr += hp // 3
        case "Frightful Presence" | "Horrifying Visage":
            if cr <= 10:
                new_effective_hp *= 1.25
                new_cr = cr_calculation(window, ac, (new_effective_hp // 1), ab_or_sdc, dpr)
                if new_cr != cr:
                    repeat += 1
                    if repeat >= 10:
                        if new_cr >= cr:
                            return effective_ac, new_effective_hp // 1, effective_ab_or_sdc, effective_dpr, new_cr
                        else:
                            return effective_ac, effective_hp // 1, effective_ab_or_sdc, effective_dpr, cr
                    else:
                        return features(window, ac, hp, new_effective_hp, ab_or_sdc, dpr, new_cr, feature, repeat)
                return effective_ac, new_effective_hp // 1, effective_ab_or_sdc, effective_dpr, new_cr
        case "Legendary Resistance":
            amount = window.entry_features[9].get()
            if amount is None or amount == "":
                amount = 0
            else:
                try:
                    amount = int(amount)
                except ValueError:
                    amount = 0
                if cr <= 4:
                    new_effective_hp += 10 * amount
                elif cr >= 5 and cr <= 10:
                    new_effective_hp += 20 * amount
                elif cr >= 11:
                    new_effective_hp += 30 * amount
                new_cr = cr_calculation(window, ac, (new_effective_hp // 1), ab_or_sdc, dpr)
                if new_cr != cr:
                    repeat += 1
                    if repeat >= 10:
                        if new_cr >= cr:
                            return effective_ac, new_effective_hp // 1, effective_ab_or_sdc, effective_dpr, new_cr
                        else:
                            return effective_ac, effective_hp // 1, effective_ab_or_sdc, effective_dpr, cr
                    else:
                        return features(window, ac, hp, new_effective_hp, ab_or_sdc, dpr, new_cr, feature, repeat)
                return effective_ac, new_effective_hp // 1, effective_ab_or_sdc, effective_dpr, new_cr
        case "Magic Resistance" | "Superior Invisibility":
            effective_ac += 2
        case "Nimble Escape":
            effective_ac += 4
            if window.offence_type.get() == "ab":
                effective_ab_or_sdc += 4
        case "Possession":
            new_effective_hp *= 2
        case "Regeneration":
            amount = window.entry_features[16].get()
            if amount is None or amount == "":
                amount = 0
            else:
                try:
                    amount = int(amount)
                except ValueError:
                    amount = 0
            new_effective_hp += 3 * amount
        case "Relentless" | "Undead Fortitude":
            if cr <= 4:
                new_effective_hp += 7
            elif cr >= 5 and cr <= 10:
                new_effective_hp += 14
            elif cr >= 11 and cr <= 16:
                new_effective_hp += 21
            elif cr >= 17:
                new_effective_hp += 28
            new_cr = cr_calculation(window, ac, (new_effective_hp // 1), ab_or_sdc, dpr)
            if new_cr != cr:
                repeat += 1
                if repeat >= 10:
                    if new_cr >= cr:
                        return effective_ac, new_effective_hp // 1, effective_ab_or_sdc, effective_dpr, new_cr
                    else:
                        return effective_ac, effective_hp // 1, effective_ab_or_sdc, effective_dpr, cr
                else:
                    return features(window, ac, hp, new_effective_hp, ab_or_sdc, dpr, new_cr, feature, repeat)
            return effective_ac, new_effective_hp // 1, effective_ab_or_sdc, effective_dpr, new_cr
        case "Shadow Stealth":
            effective_ac += 4
    cr = cr_calculation(window, effective_ac, (new_effective_hp // 1), effective_ab_or_sdc, effective_dpr)
    return effective_ac, new_effective_hp, effective_ab_or_sdc, effective_dpr, cr

def flying_speed(window, ac, effective_ac, hp, ab_or_sdc, dpr, cr, repeat = 0):
    new_effective_ac = ac
    if cr <= 10:
        new_effective_ac += 2
        new_cr = cr_calculation(window, new_effective_ac, hp, ab_or_sdc, dpr)
        if new_cr != cr:
            repeat += 1
            if repeat >= 10:
                if new_cr >= cr:
                    return new_effective_ac, new_cr
                else:
                    return effective_ac, cr
            else:
                return flying_speed(window, ac, new_effective_ac, hp, ab_or_sdc, dpr, new_cr, repeat)
        return new_effective_ac, new_cr
    return effective_ac, cr

def saving_throw_bonuses(window, ac, hp, ab_or_sdc, dpr, save):
    effective_ac = ac
    match save:
        case "3-4":
            effective_ac += 2
        case "5+":
            effective_ac += 4
    new_cr = cr_calculation(window, effective_ac, hp, ab_or_sdc, dpr)
    return effective_ac, new_cr

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

def final_results(window, ac, hp, ab_or_sdc, dpr, resist_or_immune, immune_check, vulnerable, feature_list, flying, save, con_mod):
    if ac is None or ac == "":
        ac = 0
    else:
        try:
            ac = int(ac)
        except ValueError:
            ac = 0
    if hp is None or hp == "":
        hp = 0
    else:
        try:
            hp = int(hp)
        except ValueError:
            hp = 0
    if ab_or_sdc is None or ab_or_sdc == "":
        ab_or_sdc = 0
    else:
        try:
            ab_or_sdc = int(ab_or_sdc)
        except ValueError:
            ab_or_sdc = 0
    if dpr is None or dpr == "":
        dpr = 0
    else:
        try:
            dpr = int(dpr)
        except ValueError:
            dpr = 0
    if con_mod is None or con_mod == "":
        con_mod = 0
    else:
        try:
            con_mod = int(con_mod)
        except ValueError:
            con_mod = 0
    effective_ac = ac
    effective_hp = hp
    effective_ab_or_sdc = ab_or_sdc
    effective_dpr = dpr
    cr = cr_calculation(window, ac, hp, ab_or_sdc, dpr)
    if resist_or_immune == "yes" or vulnerable == "yes":
        effective_hp, cr = resistances_immunities_and_vulnerabilities(window, effective_ac, effective_hp, effective_hp, effective_ab_or_sdc, effective_dpr, cr, resist_or_immune, immune_check, vulnerable)
    for feature_var in feature_list:
        feature = feature_var.get()
        if feature != "":
            effective_ac, effective_hp, effective_ab_or_sdc, effective_dpr, cr = features(window, effective_ac, effective_hp, effective_hp, effective_ab_or_sdc, effective_dpr, cr, feature)
    if flying == "yes":
        effective_ac, cr = flying_speed(window, effective_ac, effective_ac, effective_hp, effective_ab_or_sdc, effective_dpr, cr)
    if save == "3-4" or save == "5+":
        effective_ac, cr = saving_throw_bonuses(window, effective_ac, effective_hp, effective_ab_or_sdc, effective_dpr, save)
    window.label_effective_ac_result.configure(text = f"{int(effective_ac)}")
    window.label_effective_hp_result.configure(text = f"{int(effective_hp)}")
    window.label_effective_ab_or_sdc_result.configure(text = f"{int(effective_ab_or_sdc)}")
    window.label_effective_damage_result.configure(text = f"{int(effective_dpr)}")
    if cr <= 4:
        pb = 2
    elif cr >= 5 and cr <= 8:
        pb = 3
    elif cr >= 9 and cr <= 12:
        pb = 4
    elif cr >= 13 and cr <= 16:
        pb = 5
    elif cr >= 17 and cr <= 20:
        pb = 6
    elif cr >= 21 and cr <= 24:
        pb = 7
    elif cr >= 25 and cr <= 28:
        pb = 8
    elif cr >= 29 and cr <= 30:
        pb = 9
    window.label_proficiency_bonus_result.configure(text = f"+{int(pb)}")
    match cr:
        case 0.125:
            cr = "1/8"
        case 0.25:
            cr = "1/4"
        case 0.5:
            cr = "1/2"
    window.label_final_cr_result.configure(text = f"{cr}")
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
