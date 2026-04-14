import tkinter as tk
from tkinter import ttk
from cr_steps import hit_dice_type, hp_modifier, average_hp, average_damage, final_results, reset_window

class Window:
    def validate_number_and_negative(self, k):
        if k == "" or k == "-":
            return True
        try:
            int(k)
            return True
        except ValueError:
            return False

    def __init__(self, root):
        self.root = root
        self.nn = (self.root.register(self.validate_number_and_negative), '%P')
        self.root.title("D&D 5e Monster CR Calculator")
        self.root.resizable(width = False, height = False)

        self.frame_data = tk.Frame(master = self.root)

        self.frame_of_de_and_results = tk.Frame(master = self.frame_data)

        self.frame_of_and_de = tk.Frame(master = self.frame_of_de_and_results)

        self.frame_defensive = tk.Frame(master = self.frame_of_and_de, relief = tk.RIDGE, borderwidth = 5)
        self.frame_offensive = tk.Frame(master = self.frame_of_and_de, relief = tk.RIDGE, borderwidth = 5)

        self.frame_bonuses_and_buttons = tk.Frame(master = self.frame_data)

        self.frame_bonuses = tk.Frame(master = self.frame_bonuses_and_buttons, relief = tk.RIDGE, borderwidth = 5)
        self.frame_buttons = tk.Frame(master = self.frame_bonuses_and_buttons, relief = tk.RIDGE, borderwidth = 5)

        self.frame_stats = tk.Frame(master = self.root, relief = tk.RIDGE, borderwidth = 5)
        self.frame_features = tk.Frame(master = self.frame_data, relief = tk.RIDGE, borderwidth = 5)
        self.frame_results = tk.Frame(master = self.frame_of_de_and_results, relief = tk.RIDGE, borderwidth = 5)


        self.frame_defensive_data = tk.Frame(master = self.frame_defensive)

        self.frame_ac = tk.Frame(master = self.frame_defensive_data)
        self.frame_size = tk.Frame(master = self.frame_defensive_data)
        self.frame_con_modifier = tk.Frame(master = self.frame_defensive_data)
        self.frame_hit_dice = tk.Frame(master = self.frame_defensive_data)
        self.frame_average_hp = tk.Frame(master = self.frame_defensive_data)



        self.frame_offensive_data = tk.Frame(master = self.frame_offensive)

        self.frame_ab_or_sdc = tk.Frame(master = self.frame_offensive_data)

        self.frame_ab_or_sdc_value = tk.Frame(master = self.frame_ab_or_sdc)
        self.frame_sdc_check = tk.Frame(master = self.frame_ab_or_sdc)

        self.frame_damage_for_three_rounds = tk.Frame(master = self.frame_offensive_data)

        self.frame_round_1 = tk.Frame(master = self.frame_damage_for_three_rounds)
        self.frame_round_2 = tk.Frame(master = self.frame_damage_for_three_rounds)
        self.frame_round_3 = tk.Frame(master = self.frame_damage_for_three_rounds)

        self.frame_average_damage = tk.Frame(master = self.frame_offensive_data)



        self.frame_resistance_immunity_or_vulnerability = tk.Frame(master = self.frame_bonuses)

        self.frame_immunity_check = tk.Frame(master = self.frame_resistance_immunity_or_vulnerability)
        self.frame_vulnerability_check = tk.Frame(master = self.frame_resistance_immunity_or_vulnerability)

        self.frame_other_bonuses = tk.Frame(master = self.frame_bonuses)

        self.frame_fly_and_range = tk.Frame(master = self.frame_other_bonuses)
        self.frame_save_bonuses = tk.Frame(master = self.frame_other_bonuses)



        self.frame_cr_stats_table = tk.Frame(master = self.frame_stats)



        self.frame_features_table = tk.Frame(master = self.frame_features)



        self.frame_effective_stats = tk.Frame(master = self.frame_results)
        self.frame_possible_scores = tk.Frame(master = self.frame_results)
        self.frame_final_cr = tk.Frame(master = self.frame_results)

        self.frame_effective_stats_data = tk.Frame(master = self.frame_effective_stats)
        self.frame_possible_scores_data = tk.Frame(master = self.frame_possible_scores)

        self.create_window()

    def create_window(self):
        self.label_defence_title = tk.Label(master = self.frame_defensive, text = "Defence Stats", relief = tk.RAISED, borderwidth = 5)
        self.label_defence_title.grid(row = 0, column = 0, pady = 5)

        self.label_ac = tk.Label(master = self.frame_ac, text = "AC:")
        self.label_ac.grid(row = 0, column = 0)
        self.entry_ac = tk.Entry(master = self.frame_ac, width = 3, validate = "key", validatecommand = self.nn)
        self.entry_ac.grid(row = 0, column = 1)

        self.label_size = tk.Label(master = self.frame_size, text = "Size:")
        self.label_size.grid(row = 0, column = 0)
        self.sizes = ["Tiny", "Small", "Medium", "Large", "Huge", "Gargantuan"]
        self.size_type = tk.StringVar()
        self.combobox_size = ttk.Combobox(master = self.frame_size, textvariable = self.size_type, values = self.sizes, state = "readonly")
        self.combobox_size.bind('<<ComboboxSelected>>', lambda event: (hit_dice_type(self, self.size_type.get()), average_hp(self, self.entry_hit_dice.get())))
        self.combobox_size.grid(row = 0, column = 1)

        self.label_con_modifier = tk.Label(master = self.frame_con_modifier, text = "CON Mod:")
        self.label_con_modifier.grid(row = 0, column = 0)
        self.entry_con_modifier = tk.Entry(master = self.frame_con_modifier, width = 4, validate = "key", validatecommand = self.nn)
        self.entry_con_modifier.bind('<KeyRelease>', lambda event: (hp_modifier(self, self.entry_con_modifier.get(), self.entry_hit_dice.get()), average_hp(self, self.entry_hit_dice.get())))
        self.entry_con_modifier.grid(row = 0, column = 1)

        self.label_hit_dice = tk.Label(master = self.frame_hit_dice, text = "Hit Dice:")
        self.label_hit_dice.grid(row = 0, column = 0)
        self.entry_hit_dice = tk.Entry(master = self.frame_hit_dice, width = 3, validate = "key", validatecommand = self.nn)
        self.entry_hit_dice.bind('<KeyRelease>', lambda event: (hp_modifier(self, self.entry_con_modifier.get(), self.entry_hit_dice.get()), average_hp(self, self.entry_hit_dice.get())))
        self.entry_hit_dice.grid(row = 0, column = 1)
        self.label_con_addition = tk.Label(master = self.frame_hit_dice, text = "d4 + 0")
        self.label_con_addition.grid(row = 0, column = 2)

        self.label_average_hp = tk.Label(master = self.frame_average_hp, text = "Average HP:")
        self.label_average_hp.grid(row = 0, column = 0)
        self.label_hp_result = tk.Label(master = self.frame_average_hp, text = "0")
        self.label_hp_result.grid(row = 0, column = 1)

        self.frame_ac.grid(row = 0, column = 0, sticky = "w", padx = 5)
        self.frame_size.grid(row = 1, column = 0, sticky = "w", padx = 5)
        self.frame_con_modifier.grid(row = 2, column = 0, sticky = "w", padx = 5)
        self.frame_hit_dice.grid(row = 0, column = 1, sticky = "w", padx = 5)
        self.frame_average_hp.grid(row = 1, column = 1, sticky = "w", padx = 5)

        self.frame_defensive_data.grid(row = 1, column = 0, sticky = "w")



        self.label_offence_title = tk.Label(master = self.frame_offensive, text = "Offence Stats", relief = tk.RAISED, borderwidth = 5)
        self.label_offence_title.grid(row = 0, column = 0, pady = 5)

        self.label_ab_or_sdc = tk.Label(master = self.frame_ab_or_sdc_value, text = "AB/SDC:")
        self.label_ab_or_sdc.grid(row = 0, column = 0)
        self.entry_ab_or_sdc = tk.Entry(master = self.frame_ab_or_sdc_value, width = 3, validate = "key", validatecommand = self.nn)
        self.entry_ab_or_sdc.grid(row = 0, column = 1)
        self.label_sdc_check = tk.Label(master = self.frame_sdc_check, text = "Using SDC:")
        self.label_sdc_check.grid(row = 1, column = 0)
        self.offence_type = tk.StringVar()
        self.checkbutton_ab_or_sdc = tk.Checkbutton(master = self.frame_sdc_check, variable = self.offence_type, onvalue = "sdc", offvalue = "ab")
        self.checkbutton_ab_or_sdc.deselect()
        self.checkbutton_ab_or_sdc.grid(row = 1, column = 1)

        self.label_round_1 = tk.Label(master = self.frame_round_1, text = "Round 1:")
        self.label_round_1.grid(row = 0, column = 0)
        self.entry_round_1 = tk.Entry(master = self.frame_round_1, width = 4, validate = "key", validatecommand = self.nn)
        self.entry_round_1.bind('<KeyRelease>', lambda event: average_damage(self, self.entry_round_1.get(), self.entry_round_2.get(), self.entry_round_3.get()))
        self.entry_round_1.grid(row = 0, column = 1)
        self.label_round_2 = tk.Label(master = self.frame_round_2, text = "Round 2:")
        self.label_round_2.grid(row = 0, column = 0)
        self.entry_round_2 = tk.Entry(master = self.frame_round_2, width = 4, validate = "key", validatecommand = self.nn)
        self.entry_round_2.bind('<KeyRelease>', lambda event: average_damage(self, self.entry_round_1.get(), self.entry_round_2.get(), self.entry_round_3.get()))
        self.entry_round_2.grid(row = 0, column = 1)
        self.label_round_3 = tk.Label(master = self.frame_round_3, text = "Round 3:")
        self.label_round_3.grid(row = 0, column = 0)
        self.entry_round_3 = tk.Entry(master = self.frame_round_3, width = 4, validate = "key", validatecommand = self.nn)
        self.entry_round_3.bind('<KeyRelease>', lambda event: average_damage(self, self.entry_round_1.get(), self.entry_round_2.get(), self.entry_round_3.get()))
        self.entry_round_3.grid(row = 0, column = 1)

        self.label_average_damage = tk.Label(master = self.frame_average_damage, text = "Average damage:")
        self.label_average_damage.grid(row = 0, column = 0)
        self.label_damage_result = tk.Label(master = self.frame_average_damage, text = "0")
        self.label_damage_result.grid(row = 0, column = 1)

        self.frame_ab_or_sdc_value.grid(row = 0, column = 0, sticky = "w", padx = 5)
        self.frame_sdc_check.grid(row = 1, column = 0, sticky = "w", padx = 5)

        self.frame_ab_or_sdc.grid(row = 0, column = 0, sticky = "w")

        self.frame_round_1.grid(row = 0, column = 0, padx = 5)
        self.frame_round_2.grid(row = 0, column = 1, padx = 5)
        self.frame_round_3.grid(row = 0, column = 2, padx = 5)

        self.frame_damage_for_three_rounds.grid(row = 1, column = 0, sticky = "w")
        self.frame_average_damage.grid(row = 1, column = 1, sticky = "sw", padx = 5)

        self.frame_offensive_data.grid(row = 1, column = 0, sticky = "w")



        self.label_resistance_or_immunity = tk.Label(master = self.frame_resistance_immunity_or_vulnerability, text = "Has 3 or more damage resistances or immunities:")
        self.label_resistance_or_immunity.grid(row = 0, column = 0)
        self.resistance_or_immunity_type = tk.StringVar()
        self.checkbutton_resistance_or_immunity = tk.Checkbutton(master = self.frame_resistance_immunity_or_vulnerability, variable = self.resistance_or_immunity_type, onvalue = "yes", offvalue = "no")
        self.checkbutton_resistance_or_immunity.deselect()
        self.checkbutton_resistance_or_immunity.grid(row = 0, column = 1)
        self.label_immunity_check = tk.Label(master = self.frame_immunity_check, text = "Using immunities:")
        self.label_immunity_check.grid(row = 0, column = 0)
        self.immunity_check_type = tk.StringVar()
        self.checkbutton_immunity_check = tk.Checkbutton(master = self.frame_immunity_check, variable = self.immunity_check_type, onvalue = "immunity", offvalue = "resistance")
        self.checkbutton_immunity_check.deselect()
        self.checkbutton_immunity_check.grid(row = 0, column = 1)
        self.label_vulnerability_check = tk.Label(master = self.frame_vulnerability_check, text = "Has 3 or more damage vulnerabilities:")
        self.label_vulnerability_check.grid(row = 0, column = 0)
        self.vulnerability_check_type = tk.StringVar()
        self.checkbutton_vulnerability_check = tk.Checkbutton(master = self.frame_vulnerability_check, variable = self.vulnerability_check_type, onvalue = "yes", offvalue = "no")
        self.checkbutton_vulnerability_check.deselect()
        self.checkbutton_vulnerability_check.grid(row = 0, column = 1)

        self.label_fly_and_range = tk.Label(master = self.frame_fly_and_range, text = "Has fly speed and ranged attacks:")
        self.label_fly_and_range.grid(row = 0, column = 0)
        self.fly_and_range_type = tk.StringVar()
        self.checkbutton_fly_and_range = tk.Checkbutton(master = self.frame_fly_and_range, variable = self.fly_and_range_type, onvalue = "yes", offvalue = "no")
        self.checkbutton_fly_and_range.deselect()
        self.checkbutton_fly_and_range.grid(row = 0, column = 1)

        self.label_save_bonuses = tk.Label(master = self.frame_save_bonuses, text = "Amount of saves:")
        self.label_save_bonuses.grid(row = 0, column = 0)
        self.save_amount = ["0-2", "3-4", "5+"]
        self.save_bonuses_type = tk.StringVar()
        self.combobox_save_bonuses = ttk.Combobox(master = self.frame_save_bonuses, textvariable = self.save_bonuses_type, values = self.save_amount, state = "readonly")
        self.combobox_save_bonuses.grid(row = 0, column = 1)

        self.frame_resistance_immunity_or_vulnerability.grid(row = 0, column = 0, sticky = "w", padx = 5)

        self.frame_immunity_check.grid(row = 1, column = 0, sticky = "w")
        self.frame_vulnerability_check.grid(row = 2, column = 0, sticky = "w")

        self.frame_other_bonuses.grid(row = 0, column = 1, sticky = "nw")

        self.frame_fly_and_range.grid(row = 0, column = 1, sticky = "w", padx = 5)
        self.frame_save_bonuses.grid(row = 1, column = 1, sticky = "nw", padx = 5)



        self.button_submit = tk.Button(master = self.frame_buttons, text = "Submit", command = lambda: final_results(self, self.entry_ac.get(), self.label_hp_result.cget("text"), self.entry_ab_or_sdc.get(), self.label_damage_result.cget("text"), self.resistance_or_immunity_type.get(), self.immunity_check_type.get(), self.vulnerability_check_type.get(), self.feature_types, self.fly_and_range_type.get(), self.save_bonuses_type.get(), self.entry_con_modifier.get()))
        self.button_submit.grid(row = 0, column = 0)
        self.button_clear = tk.Button(master = self.frame_buttons, text = "Clear", command = lambda: reset_window(self))
        self.button_clear.grid(row = 0, column = 1)



        self.label_stats_title = tk.Label(master = self.frame_stats, text = "Stat Table", relief = tk.RAISED, borderwidth = 5)
        self.label_stats_title.grid(row = 0, column = 0, pady = 5)

        self.stats = {
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
                )
            }

        self.create_stat_table()



        self.label_features_title = tk.Label(master = self.frame_features, text = "Features Table", relief = tk.RAISED, borderwidth = 5)
        self.label_features_title.grid(row = 0, column = 0, pady = 5)

        self.features = (
            ("Aggressive", "Effective D/R + 2", False),
            ("Ambusher", "Effective AB + 1", False),
            ("Avoidance", "Effective AC + 1", False),
            ("Blood Frenzy", "Effective AB + 4", False),
            ("Constrict", "Effective AC + 1", False),
            ("Damage Transfer", "Effective HP * 2, and Effective D/R + HP / 3", False),
            ("Fiendish Blessing", "Determines the monster's Charisma modifier", True),
            ("Frightful Presence", "Effective HP * 1.25 if cr \u2264 10", False),
            ("Horrifying Visage", "Effective HP * 1.25 if cr \u2264 10", False),
            ("Legendary Resistance", "Effective HP + (10 if cr \u2264 4) (20 if 5 \u2264 cr \u2264 10) (30 if 11 \u2264 cr) per use", True),
            ("Magic Resistance", "Effective AC + 2", False),
            ("Nimble Escape", "Effective AC + 4, and Effective AB + 4 (if the monster hides every round)", False),
            ("Pack Tactics", "Effective AB + 1", False),
            ("Parry", "Effective AC + 1", False),
            ("Possession", "Effective HP * 2", False),
            ("Psychic Defence", "Determines the monster's Wisdom modifier (if the monster isn't wearing armor or wielding a shield)", True),
            ("Regeneration", "Effective HP + 3 x the number of hit points the monster regenerates each round", True),
            ("Relentless", "Effective HP + (7 if cr \u2264 4) (14 if 5 \u2264 cr \u2264 10) (21 if 11 \u2264 cr \u2264 16) (28 if 17 \u2264 cr)", False),
            ("Shadow Stealth", "Effective AC + 4", False),
            ("Stench", "Effective AC + 1", False),
            ("Superior Invisibility", "Effective AC + 2", False),
            ("Undead Fortitude", "Effective HP + (7 if cr \u2264 4) (14 if 5 \u2264 cr \u2264 10) (21 if 11 \u2264 cr \u2264 16) (28 if 17 \u2264 cr)", False),
            ("Web", "Effective AC + 1", False),
            )

        self.create_features_table()



        self.label_effective_stats_title = tk.Label(master = self.frame_effective_stats, text = "Effective Stats", relief = tk.RAISED, borderwidth = 5)
        self.label_effective_stats_title.grid(row = 0, column = 0, pady = 5)
        self.label_possible_scores_title = tk.Label(master = self.frame_possible_scores, text = "Possible Scores", relief = tk.RAISED, borderwidth = 5)
        self.label_possible_scores_title.grid(row = 0, column = 0, padx = 5, pady = 5)

        self.label_effective_ac = tk.Label(master = self.frame_effective_stats_data, text = "Effective AC:")
        self.label_effective_ac.grid(row = 0, column = 0, sticky = "w", padx = 5)
        self.label_effective_ac_result = tk.Label(master = self.frame_effective_stats_data, text = "0")
        self.label_effective_ac_result.grid(row = 0, column = 1, sticky = "w")
        self.label_effective_hp = tk.Label(master = self.frame_effective_stats_data, text = "Effective HP:")
        self.label_effective_hp.grid(row = 1, column = 0, sticky = "w", padx = 5)
        self.label_effective_hp_result = tk.Label(master = self.frame_effective_stats_data, text = "0")
        self.label_effective_hp_result.grid(row = 1, column = 1, sticky = "w")
        self.label_effective_ab_or_sdc = tk.Label(master = self.frame_effective_stats_data, text = "Effective AB/SDC:")
        self.label_effective_ab_or_sdc.grid(row = 2, column = 0, sticky = "w", padx = 5)
        self.label_effective_ab_or_sdc_result = tk.Label(master = self.frame_effective_stats_data, text = "0")
        self.label_effective_ab_or_sdc_result.grid(row = 2, column = 1, sticky = "w")
        self.label_effective_damage = tk.Label(master = self.frame_effective_stats_data, text = "Effective damage:")
        self.label_effective_damage.grid(row = 3, column = 0, sticky = "w", padx = 5)
        self.label_effective_damage_result = tk.Label(master = self.frame_effective_stats_data, text = "0")
        self.label_effective_damage_result.grid(row = 3, column = 1, sticky = "w")
        self.label_proficiency_bonus = tk.Label(master = self.frame_effective_stats_data, text = "Proficiency Bonus:")
        self.label_proficiency_bonus.grid(row = 4, column = 0, sticky = "w", padx = 5)
        self.label_proficiency_bonus_result = tk.Label(master = self.frame_effective_stats_data, text = "+2")
        self.label_proficiency_bonus_result.grid(row = 4, column = 1, sticky = "w")

        self.label_possible_con = tk.Label(master = self.frame_possible_scores_data, text = "CON:")
        self.label_possible_con.grid(row = 0, column = 0, sticky = "w")
        self.label_possible_con_result = tk.Label(master = self.frame_possible_scores_data, text = "0")
        self.label_possible_con_result.grid(row = 0, column = 1, sticky = "w", padx = 5)
        self.label_possible_attack_stat = tk.Label(master = self.frame_possible_scores_data, text = "Attack Stat:")
        self.label_possible_attack_stat.grid(row = 1, column = 0, sticky = "w")
        self.label_possible_attack_stat_result = tk.Label(master = self.frame_possible_scores_data, text = "0")
        self.label_possible_attack_stat_result.grid(row = 1, column = 1, sticky = "w", padx = 5)
        self.label_possible_cha = tk.Label(master = self.frame_possible_scores_data, text = "CHA:")
        self.label_possible_cha.grid(row = 2, column = 0, sticky = "w")
        self.label_possible_cha_result = tk.Label(master = self.frame_possible_scores_data, text = "0")
        self.label_possible_cha_result.grid(row = 2, column = 1, sticky = "w", padx = 5)
        self.label_possible_wis = tk.Label(master = self.frame_possible_scores_data, text = "WIS:")
        self.label_possible_wis.grid(row = 3, column = 0, sticky = "w")
        self.label_possible_wis_result = tk.Label(master = self.frame_possible_scores_data, text = "0")
        self.label_possible_wis_result.grid(row = 3, column = 1, sticky = "w", padx = 5)

        self.frame_effective_stats_data.grid(row = 1, column = 0)
        self.frame_possible_scores_data.grid(row = 1, column = 0)

        self.label_final_cr = tk.Label(master = self.frame_final_cr, text = "Final CR:")
        self.label_final_cr.grid(row = 0, column = 0, padx = 5)
        self.label_final_cr_result = tk.Label(master = self.frame_final_cr, text = "0")
        self.label_final_cr_result.grid(row = 0, column = 1)

        self.frame_effective_stats.grid(row = 0, column = 0, sticky = "n")
        self.frame_possible_scores.grid(row = 0, column = 1, sticky = "n")
        self.frame_final_cr.grid(row = 1, column = 0, sticky = "w")


        self.frame_defensive.grid(row = 0, column = 0, sticky = "w", padx = 5, pady = 5)
        self.frame_offensive.grid(row = 1, column = 0, sticky = "w", padx = 5, pady = 5)

        self.frame_of_and_de.grid(row = 0, column = 0, sticky = "w")

        self.frame_bonuses.grid(row = 0, column = 0, sticky = "w", padx = 5, pady = 5)
        self.frame_buttons.grid(row = 0, column = 1, sticky = "se", padx = 5, pady = 5)

        self.frame_bonuses_and_buttons.grid(row = 2, column = 0, sticky = "w")

        self.frame_stats.grid(row = 0, column = 1, sticky = "n", padx = 5, pady = 5)
        self.frame_features.grid(row = 3, column = 0, padx = 5, pady = 5)
        self.frame_results.grid(row = 0, column = 1, sticky = "ne", padx = 5, pady = 5)

        self.frame_of_de_and_results.grid(row = 0, column = 0, sticky = "nw")

        self.frame_data.grid(row = 0, column = 0, sticky = "n")

    def create_stat_table(self):
        self.stat_labels = []
        column = 0
        for stat in self.stats:
            row = 0
            column_labels = []
            for value in self.stats[stat]:
                if row % 2 == 0:
                    label_stat = tk.Label(master = self.frame_cr_stats_table, text = f"{value}", bg = "white")
                else:
                    label_stat = tk.Label(master = self.frame_cr_stats_table, text = f"{value}", bg = "lightgray")
                label_stat.grid(row = row, column = column, padx = 5)
                column_labels.append(label_stat)
                row += 1
            self.stat_labels.append(column_labels)
            column += 1
        self.frame_cr_stats_table.grid(row = 1, column = 0)

    def create_features_table(self):
        self.feature_types = []
        self.checkbutton_features = []
        self.entry_features = []
        self.label_features = []
        for i, feature in enumerate(self.features):
            title, description, has_entry = feature
            feature_type = tk.StringVar()
            self.feature_types.append(feature_type)
            checkbutton_feature = tk.Checkbutton(master = self.frame_features_table, variable = feature_type, onvalue = title, offvalue = "")
            checkbutton_feature.deselect()
            checkbutton_feature.grid(row = i, column = 0)
            self.checkbutton_features.append(checkbutton_feature)
            if has_entry:
                entry_feature = tk.Entry(master = self.frame_features_table, width = 4, validate = "key", validatecommand = self.nn)
                entry_feature.grid(row = i, column = 1)
                self.entry_features.append(entry_feature)
            else:
                self.entry_features.append(None)
            if i % 2 == 0:
                label_feature = tk.Label(master = self.frame_features_table, text = f"{title}: {description}.", bg = "white")
            else:
                label_feature = tk.Label(master = self.frame_features_table, text = f"{title}: {description}.", bg = "lightgray")
            label_feature.grid(row = i, column = 2, sticky = "w", padx = 5)
            self.label_features.append(label_feature)
        self.frame_features_table.grid(row = 1, column = 0)
