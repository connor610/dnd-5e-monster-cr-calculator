import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("D&D 5e Monster CR Calculator")
window.resizable(width = False, height = False)

frame_data = tk.Frame(master = window)

frame_of_de_and_results = tk.Frame(master = frame_data)

frame_of_and_de = tk.Frame(master = frame_of_de_and_results)

frame_defensive = tk.Frame(master = frame_of_and_de, relief = tk.RIDGE, borderwidth = 5)
frame_offensive = tk.Frame(master = frame_of_and_de, relief = tk.RIDGE, borderwidth = 5)

frame_bonuses_and_buttons = tk.Frame(master = frame_data)

frame_bonuses = tk.Frame(master = frame_bonuses_and_buttons, relief = tk.RIDGE, borderwidth = 5)
frame_buttons = tk.Frame(master = frame_bonuses_and_buttons, relief = tk.RIDGE, borderwidth = 5)

frame_stats = tk.Frame(master = window, relief = tk.RIDGE, borderwidth = 5)
frame_features = tk.Frame(master = frame_data, relief = tk.RIDGE, borderwidth = 5)
frame_results = tk.Frame(master = frame_of_de_and_results, relief = tk.RIDGE, borderwidth = 5)


label_defence_title = tk.Label(master = frame_defensive, text = "Defence Stats", relief = tk.RAISED, borderwidth = 5)
label_defence_title.grid(row = 0, column = 0, pady = 5)

frame_defensive_data = tk.Frame(master = frame_defensive)

frame_ac = tk.Frame(master = frame_defensive_data)
frame_size = tk.Frame(master = frame_defensive_data)
frame_con_modifier = tk.Frame(master = frame_defensive_data)
frame_hit_dice = tk.Frame(master = frame_defensive_data)
frame_average_hp = tk.Frame(master = frame_defensive_data)

label_ac = tk.Label(master = frame_ac, text = "AC:")
label_ac.grid(row = 0, column = 0)
entry_ac = tk.Entry(master = frame_ac, width = 3)
entry_ac.grid(row = 0, column = 1)

label_size = tk.Label(master = frame_size, text = "Size:")
label_size.grid(row = 0, column = 0)
sizes = ["Tiny", "Small", "Medium", "Large", "Huge", "Gargantuan"]
size_type = tk.StringVar()
combobox_size = ttk.Combobox(master = frame_size, textvariable = size_type, values = sizes, state = "readonly")
combobox_size.grid(row = 0, column = 1)

label_con_modifier = tk.Label(master = frame_con_modifier, text = "CON Mod:")
label_con_modifier.grid(row = 0, column = 0)
entry_con_modifier = tk.Entry(master = frame_con_modifier, width = 4)
entry_con_modifier.grid(row = 0, column = 1)

label_hit_dice = tk.Label(master = frame_hit_dice, text = "Hit Dice:")
label_hit_dice.grid(row = 0, column = 0)
entry_hit_dice = tk.Entry(master = frame_hit_dice, width = 3)
entry_hit_dice.grid(row = 0, column = 1)
label_con_addition = tk.Label(master = frame_hit_dice, text = "d4 + 0")
label_con_addition.grid(row = 0, column = 2)

label_average_hp = tk.Label(master = frame_average_hp, text = "Average HP:")
label_average_hp.grid(row = 0, column = 0)
label_hp_result = tk.Label(master = frame_average_hp, text = "0")
label_hp_result.grid(row = 0, column = 1)

frame_ac.grid(row = 0, column = 0, sticky = "w", padx = 5)
frame_size.grid(row = 1, column = 0, sticky = "w", padx = 5)
frame_con_modifier.grid(row = 2, column = 0, sticky = "w", padx = 5)
frame_hit_dice.grid(row = 0, column = 1, sticky = "w", padx = 5)
frame_average_hp.grid(row = 1, column = 1, sticky = "w", padx = 5)

frame_defensive_data.grid(row = 1, column = 0, sticky = "w")



label_offence_title = tk.Label(master = frame_offensive, text = "Offence Stats", relief = tk.RAISED, borderwidth = 5)
label_offence_title.grid(row = 0, column = 0, pady = 5)

frame_offensive_data = tk.Frame(master = frame_offensive)

frame_ab_or_sdc = tk.Frame(master = frame_offensive_data)

frame_ab_or_sdc_value = tk.Frame(master = frame_ab_or_sdc)
frame_sdc_check = tk.Frame(master = frame_ab_or_sdc)

frame_damage_for_three_rounds = tk.Frame(master = frame_offensive_data)

frame_round_1 = tk.Frame(master = frame_damage_for_three_rounds)
frame_round_2 = tk.Frame(master = frame_damage_for_three_rounds)
frame_round_3 = tk.Frame(master = frame_damage_for_three_rounds)

frame_average_damage = tk.Frame(master = frame_offensive_data)

label_ab_or_sdc = tk.Label(master = frame_ab_or_sdc_value, text = "AB/SDC:")
label_ab_or_sdc.grid(row = 0, column = 0)
entry_ab_or_sdc = tk.Entry(master = frame_ab_or_sdc_value, width = 3)
entry_ab_or_sdc.grid(row = 0, column = 1)
label_sdc_check = tk.Label(master = frame_sdc_check, text = "Using SDC:")
label_sdc_check.grid(row = 1, column = 0)
offence_type = tk.StringVar()
checkbutton_ab_or_sdc = tk.Checkbutton(master = frame_sdc_check, variable = offence_type, onvalue = "sdc", offvalue = "ab")
checkbutton_ab_or_sdc.grid(row = 1, column = 1)

label_round_1 = tk.Label(master = frame_round_1, text = "Round 1:")
label_round_1.grid(row = 0, column = 0)
entry_round_1 = tk.Entry(master = frame_round_1, width = 4)
entry_round_1.grid(row = 0, column = 1)
label_round_2 = tk.Label(master = frame_round_2, text = "Round 2:")
label_round_2.grid(row = 0, column = 0)
entry_round_2 = tk.Entry(master = frame_round_2, width = 4)
entry_round_2.grid(row = 0, column = 1)
label_round_3 = tk.Label(master = frame_round_3, text = "Round 3:")
label_round_3.grid(row = 0, column = 0)
entry_round_3 = tk.Entry(master = frame_round_3, width = 4)
entry_round_3.grid(row = 0, column = 1)

label_average_damage = tk.Label(master = frame_average_damage, text = "Average damage:")
label_average_damage.grid(row = 0, column = 0)
label_damage_result = tk.Label(master = frame_average_damage, text = "0")
label_damage_result.grid(row = 0, column = 1)

frame_ab_or_sdc_value.grid(row = 0, column = 0, sticky = "w", padx = 5)
frame_sdc_check.grid(row = 1, column = 0, sticky = "w", padx = 5)

frame_ab_or_sdc.grid(row = 0, column = 0, sticky = "w")

frame_round_1.grid(row = 0, column = 0, padx = 5)
frame_round_2.grid(row = 0, column = 1, padx = 5)
frame_round_3.grid(row = 0, column = 2, padx = 5)

frame_damage_for_three_rounds.grid(row = 1, column = 0, sticky = "w")
frame_average_damage.grid(row = 0, column = 1, sticky = "nw", padx = 5)

frame_offensive_data.grid(row = 1, column = 0, sticky = "w")



frame_resistance_or_immunity = tk.Frame(master = frame_bonuses)

frame_immunity_check = tk.Frame(master = frame_resistance_or_immunity)

frame_fly_and_range = tk.Frame(master = frame_bonuses)
frame_save_bonuses = tk.Frame(master = frame_bonuses)

label_resistance_or_immunity = tk.Label(master = frame_resistance_or_immunity, text = "Has 3 or more damage resistances or immunities:")
label_resistance_or_immunity.grid(row = 0, column = 0)
resistance_or_immunity_type = tk.StringVar()
checkbutton_resistance_or_immunity = tk.Checkbutton(master = frame_resistance_or_immunity, variable = resistance_or_immunity_type, onvalue = "yes", offvalue = "no")
checkbutton_resistance_or_immunity.grid(row = 0, column = 1)
label_immunity_check = tk.Label(master = frame_immunity_check, text = "Using immunities:")
label_immunity_check.grid(row = 1, column = 0)
immunity_check_type = tk.StringVar()
checkbutton_immunity_check = tk.Checkbutton(master = frame_immunity_check, variable = immunity_check_type, onvalue = "immunity", offvalue = "resistance")
checkbutton_immunity_check.grid(row = 1, column = 1)

label_fly_and_range = tk.Label(master = frame_fly_and_range, text = "Has fly speed and ranged attacks:")
label_fly_and_range.grid(row = 0, column = 0)
fly_and_range_type = tk.StringVar()
checkbutton_fly_and_range = tk.Checkbutton(master = frame_fly_and_range, variable = fly_and_range_type, onvalue = "yes", offvalue = "no")
checkbutton_fly_and_range.grid(row = 0, column = 1)

label_save_bonuses = tk.Label(master = frame_save_bonuses, text = "Amount of saves:")
label_save_bonuses.grid(row = 0, column = 0)
save_amount = ["0-2", "3-4", "5+"]
save_bonuses_type = tk.StringVar()
combobox_save_bonuses = ttk.Combobox(master = frame_save_bonuses, textvariable = save_bonuses_type, values = save_amount, state = "readonly")
combobox_save_bonuses.grid(row = 0, column = 1)

frame_resistance_or_immunity.grid(row = 0, column = 0, sticky = "w", padx = 5)

frame_immunity_check.grid(row = 1, column = 0, sticky = "w")

frame_fly_and_range.grid(row = 1, column = 0, sticky = "w", padx = 5)
frame_save_bonuses.grid(row = 0, column = 1, sticky = "nw", padx = 5)



button_submit = tk.Button(master = frame_buttons, text = "Submit")
button_submit.grid(row = 0, column = 0)
button_clear = tk.Button(master = frame_buttons, text = "Clear")
button_clear.grid(row = 0, column = 1)



label_stats_title = tk.Label(master = frame_stats, text = "Stat Table", relief = tk.RAISED, borderwidth = 5)
label_stats_title.grid(row = 0, column = 0, pady = 5)

frame_cr_stats_table = tk.Frame(master = frame_stats)

stats = {
    "cr": (
        "Challenge\nRating",
        "0",
        "1/8",
        "1/4",
        "1/2",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
        "18",
        "19",
        "20",
        "21",
        "22",
        "23",
        "24",
        "25",
        "26",
        "27",
        "28",
        "29",
        "30",
        ),
    "ac": (
        "Armour\nClass",
        "\u2264 13",
        "13",
        "13",
        "13",
        "13",
        "13",
        "13",
        "14",
        "15",
        "15",
        "15",
        "16",
        "16",
        "17",
        "17",
        "17",
        "18",
        "18",
        "18",
        "18",
        "19",
        "19",
        "19",
        "19",
        "19",
        "19",
        "19",
        "19",
        "19",
        "19",
        "19",
        "19",
        "19",
        "19",
        ),
    "hp": (
        "Hit\nPoints",
        "1-6",
        "7-35",
        "36-49",
        "50-70",
        "71-85",
        "86-100",
        "101-115",
        "116-130",
        "131-145",
        "146-160",
        "161-175",
        "176-190",
        "191-205",
        "206-220",
        "221-235",
        "236-250",
        "251-265",
        "266-280",
        "281-295",
        "296-310",
        "311-325",
        "326-340",
        "341-355",
        "356-400",
        "401-445",
        "446-490",
        "491-535",
        "536-580",
        "581-625",
        "626-670",
        "671-715",
        "716-760",
        "761-805",
        "806-850",
        ),
    "at": (
        "Attack\nBonus",
        "\u2264 +3",
        "+3",
        "+3",
        "+3",
        "+3",
        "+3",
        "+4",
        "+5",
        "+6",
        "+6",
        "+6",
        "+7",
        "+7",
        "+7",
        "+8",
        "+8",
        "+8",
        "+8",
        "+8",
        "+9",
        "+10",
        "+10",
        "+10",
        "+10",
        "+11",
        "+11",
        "+11",
        "+12",
        "+12",
        "+12",
        "+13",
        "+13",
        "+13",
        "+14",
        ),
    "d/r": (
        "Damage/\nRound",
        "0-1",
        "2-3",
        "4-5",
        "6-8",
        "9-14",
        "15-20",
        "21-26",
        "27-32",
        "33-38",
        "39-44",
        "45-50",
        "51-56",
        "57-62",
        "63-68",
        "69-74",
        "75-80",
        "81-86",
        "87-92",
        "93-98",
        "99-104",
        "105-110",
        "111-116",
        "117-122",
        "123-140",
        "141-158",
        "159-176",
        "177-194",
        "195-212",
        "213-230",
        "231-248",
        "249-266",
        "267-284",
        "285-302",
        "303-320",
        ),
    "sdc": (
        "Save\nDifficulty\nClass",
        "\u2264 13",
        "13",
        "13",
        "13",
        "13",
        "13",
        "13",
        "14",
        "15",
        "15",
        "15",
        "16",
        "16",
        "16",
        "17",
        "17",
        "18",
        "18",
        "18",
        "18",
        "19",
        "19",
        "19",
        "19",
        "20",
        "20",
        "20",
        "21",
        "21",
        "21",
        "22",
        "22",
        "22",
        "23",
        ),
    }
column = 0
for stat in stats:
    row = 0
    for value in stats[stat]:
        if row % 2 == 0:
            label_stat = tk.Label(master = frame_cr_stats_table, text = f"{value}", bg = "white")
        else:
            label_stat = tk.Label(master = frame_cr_stats_table, text = f"{value}", bg = "lightgray")
        label_stat.grid(row = row, column = column, padx = 5)
        row += 1
    column += 1

frame_cr_stats_table.grid(row = 1, column = 0)



label_features_title = tk.Label(master = frame_features, text = "Features Table", relief = tk.RAISED, borderwidth = 5)
label_features_title.grid(row = 0, column = 0, pady = 5)

frame_features_table = tk.Frame(master = frame_features)

features = (
    ("Aggressive", "Effective D/R + 2", False),
    ("Ambusher", "Effective AB + 1", False),
    ("Avoidance", "Effective AC + 1", False),
    ("Blood Frenzy", "Effective AB + 4", False),
    ("Constrict", "Effective AC + 1", False),
    ("Damage Transfer", "Effective HP * 2, and Effective D/R + HP / 3", False),
    ("Fiendish Blessing", "Determines the monster's Charisma modifier", True),
    ("Frightful Presence", "Effective HP * 1.25 if cr \u2264 10", False),
    ("Horrifying Visage", "Effective HP * 1.25 if cr \u2264 10", False),
    ("Legendary Resistance", "Effective HP + (10 if 1 \u2264 cr \u2264 4) (20 if 5 \u2264 cr \u2264 10) (30 if 11 \u2264 cr) per use", True),
    ("Magic Resistance", "Effective AC + 2", False),
    ("Nimble Escape", "Effective AC + 4, and Effective AB + 4 (if the monster hides every round)", False),
    ("Pack Tactics", "Effective AB + 1", False),
    ("Parry", "Effective AC + 1", False),
    ("Possession", "Effective HP * 2", False),
    ("Psychic Defense", "Determines the monster's Wisdom modifier (if the monster isn't wearing armor or wielding a shield)", True),
    ("Regeneration", "Effective HP + 3 x the number of hit points the monster regenerates each round", True),
    ("Relentless", "Effective HP + (7 if 1 \u2264 cr \u2264 4) (14 if 5 \u2264 cr \u2264 10) (21 if 11 \u2264 cr \u2264 16) (28 if 17 \u2264 cr)", False),
    ("Shadow Stealth", "Effective AC + 4", False),
    ("Stench", "Effective AC + 1", False),
    ("Superior Invisibility", "Effective AC + 2", False),
    ("Undead Fortitude", "Effective HP + (7 if 1 \u2264 cr \u2264 4) (14 if 5 \u2264 cr \u2264 10) (21 if 11 \u2264 cr \u2264 16) (28 if 17 \u2264 cr)", False),
    ("Web", "Effective AC + 1", False),
    )
for i in range(len(features) - 1):
    feature_type = tk.StringVar()
    checkbutton_feature = tk.Checkbutton(master = frame_features_table, variable = offence_type, onvalue = f"{features[i][0]}", offvalue = None)
    checkbutton_feature.grid(row = i, column = 0)
    if features[i][2] == True:
        entry_feature = tk.Entry(master = frame_features_table, width = 4)
        entry_feature.grid(row = i, column = 1)
    if i % 2 == 0:
        label_feature = tk.Label(master = frame_features_table, text = f"{features[i][0]}: {features[i][1]}.", bg = "white")
    else:
        label_feature = tk.Label(master = frame_features_table, text = f"{features[i][0]}: {features[i][1]}.", bg = "lightgray")
    label_feature.grid(row = i, column = 2, sticky = "w", padx = 5)

frame_features_table.grid(row = 1, column = 0)



frame_effective_stats = tk.Frame(master = frame_results)
frame_possible_scores = tk.Frame(master = frame_results)
frame_final_cr = tk.Frame(master = frame_results)

label_effective_stats_title = tk.Label(master = frame_effective_stats, text = "Effective Stats", relief = tk.RAISED, borderwidth = 5)
label_effective_stats_title.grid(row = 0, column = 0, pady = 5)
label_possible_scores_title = tk.Label(master = frame_possible_scores, text = "Possible Scores", relief = tk.RAISED, borderwidth = 5)
label_possible_scores_title.grid(row = 0, column = 0, padx = 5, pady = 5)

frame_effective_stats_data = tk.Frame(master = frame_effective_stats)
frame_possible_scores_data = tk.Frame(master = frame_possible_scores)

label_effective_ac = tk.Label(master = frame_effective_stats_data, text = "Effective AC:")
label_effective_ac.grid(row = 0, column = 0, sticky = "w", padx = 5)
label_effective_ac_result = tk.Label(master = frame_effective_stats_data, text = "0")
label_effective_ac_result.grid(row = 0, column = 1, sticky = "w")
label_effective_hp = tk.Label(master = frame_effective_stats_data, text = "Effective HP:")
label_effective_hp.grid(row = 1, column = 0, sticky = "w", padx = 5)
label_effective_hp_result = tk.Label(master = frame_effective_stats_data, text = "0")
label_effective_hp_result.grid(row = 1, column = 1, sticky = "w")
label_effective_ab_or_sdc = tk.Label(master = frame_effective_stats_data, text = "Effective AB/SDC:")
label_effective_ab_or_sdc.grid(row = 2, column = 0, sticky = "w", padx = 5)
label_effective_ab_or_sdc_result = tk.Label(master = frame_effective_stats_data, text = "0")
label_effective_ab_or_sdc_result.grid(row = 2, column = 1, sticky = "w")
label_effective_damage = tk.Label(master = frame_effective_stats_data, text = "Effective damage:")
label_effective_damage.grid(row = 3, column = 0, sticky = "w", padx = 5)
label_effective_damage_result = tk.Label(master = frame_effective_stats_data, text = "0")
label_effective_damage_result.grid(row = 3, column = 1, sticky = "w")
label_proficiency_bonus = tk.Label(master = frame_effective_stats_data, text = "Proficiency Bonus:")
label_proficiency_bonus.grid(row = 4, column = 0, sticky = "w", padx = 5)
label_proficiency_bonus_result = tk.Label(master = frame_effective_stats_data, text = "+2")
label_proficiency_bonus_result.grid(row = 4, column = 1, sticky = "w")

label_possible_con = tk.Label(master = frame_possible_scores_data, text = "CON:")
label_possible_con.grid(row = 0, column = 0, sticky = "w")
label_possible_con_result = tk.Label(master = frame_possible_scores_data, text = "0")
label_possible_con_result.grid(row = 0, column = 1, sticky = "w", padx = 5)
label_possible_attack_stat = tk.Label(master = frame_possible_scores_data, text = "Attack Stat:")
label_possible_attack_stat.grid(row = 1, column = 0, sticky = "w")
label_possible_attack_stat_result = tk.Label(master = frame_possible_scores_data, text = "0")
label_possible_attack_stat_result.grid(row = 1, column = 1, sticky = "w", padx = 5)
label_possible_cha = tk.Label(master = frame_possible_scores_data, text = "CHA:")
label_possible_cha.grid(row = 2, column = 0, sticky = "w")
label_possible_cha_result = tk.Label(master = frame_possible_scores_data, text = "0")
label_possible_cha_result.grid(row = 2, column = 1, sticky = "w", padx = 5)
label_possible_wis = tk.Label(master = frame_possible_scores_data, text = "WIS:")
label_possible_wis.grid(row = 3, column = 0, sticky = "w")
label_possible_wis_result = tk.Label(master = frame_possible_scores_data, text = "0")
label_possible_wis_result.grid(row = 3, column = 1, sticky = "w", padx = 5)

frame_effective_stats_data.grid(row = 1, column = 0)
frame_possible_scores_data.grid(row = 1, column = 0)

label_final_cr = tk.Label(master = frame_final_cr, text = "Final CR:")
label_final_cr.grid(row = 0, column = 0, padx = 5)
label_final_cr_result = tk.Label(master = frame_final_cr, text = "0")
label_final_cr_result.grid(row = 0, column = 1)

frame_effective_stats.grid(row = 0, column = 0, sticky = "n")
frame_possible_scores.grid(row = 0, column = 1, sticky = "n")
frame_final_cr.grid(row = 1, column = 0, sticky = "w")


frame_defensive.grid(row = 0, column = 0, sticky = "w", padx = 5, pady = 5)
frame_offensive.grid(row = 1, column = 0, sticky = "w", padx = 5, pady = 5)

frame_of_and_de.grid(row = 0, column = 0, sticky = "w")

frame_bonuses.grid(row = 0, column = 0, sticky = "w", padx = 5, pady = 5)
frame_buttons.grid(row = 0, column = 1, sticky = "se", padx = 5, pady = 5)

frame_bonuses_and_buttons.grid(row = 2, column = 0, sticky = "w")

frame_stats.grid(row = 0, column = 1, sticky = "n", padx = 5, pady = 5)
frame_features.grid(row = 3, column = 0, padx = 5, pady = 5)
frame_results.grid(row = 0, column = 1, sticky = "ne", padx = 5, pady = 5)

frame_of_de_and_results.grid(row = 0, column = 0, sticky = "nw")

frame_data.grid(row = 0, column = 0, sticky = "n")



window.mainloop()
