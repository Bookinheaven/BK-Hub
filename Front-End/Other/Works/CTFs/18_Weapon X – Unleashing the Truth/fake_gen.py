# import base64

# import base64

# def encode_flag(flag, times=15):
#     encoded = flag.encode()
#     for _ in range(times):
#         encoded = base64.b64encode(encoded)
#     return encoded.decode()

# def main():
#     flags = [
#         "MC_CTF:adamantium_wrath", "MC_CTF:logan_fury", "MC_CTF:berserker_mode",
#         "MC_CTF:weapon_x_project", "MC_CTF:xmen_resistance", "MC_CTF:wolverine_warrior",
#         "MC_CTF:claws_unleashed", "MC_CTF:logan_survivor", "MC_CTF:feral_instincts",
#         "MC_CTF:wild_hunter_x", "MC_CTF:rage_within", "MC_CTF:canadian_beast",
#         "MC_CTF:team_x_escape", "MC_CTF:snikt_master", "MC_CTF:mutant_avenger",
#         "MC_CTF:logan_vs_sentinels", "MC_CTF:healing_factor_x", "MC_CTF:adamantium_blood",
#         "MC_CTF:logan_unbreakable", "MC_CTF:dark_wolverine", "MC_CTF:wolverine_xforce",
#         "MC_CTF:logan_shadow", "MC_CTF:wolverine_vs_omega_red", "MC_CTF:mutant_mercenary",
#         "MC_CTF:wolverine_experiment", "MC_CTF:logan_battlefield", "MC_CTF:clawed_through_time",
#         "MC_CTF:regeneration_overdrive", "MC_CTF:snikt_in_the_night", "MC_CTF:logan_vs_ninjas",
#         "MC_CTF:ultimate_wolverine", "MC_CTF:xmen_legends", "MC_CTF:wolverine_inferno",
#         "MC_CTF:logan_no_memory", "MC_CTF:beast_mode_snikt", "MC_CTF:weapon_x_initiative",
#         "MC_CTF:logan_ghost", "MC_CTF:wolverine_lone_warrior", "MC_CTF:xmen_berserker",
#         "MC_CTF:logan_never_forgets", "MC_CTF:wolverine_vs_sabretooth", "MC_CTF:logan_hunter",
#         "MC_CTF:mutant_assassin_x", "MC_CTF:logan_tactical", "MC_CTF:adamantium_tiger",
#         "MC_CTF:xmen_blacklist", "MC_CTF:logan_resurrection", "MC_CTF:wolverine_vs_deadpool",
#         "MC_CTF:mutant_rage", "MC_CTF:logan_fangs", "MC_CTF:wolverine_immortal",
#         "MC_CTF:logan_samurai", "MC_CTF:logan_alpha_flight", "MC_CTF:adamantium_wound",
#         "MC_CTF:logan_fury_unleashed", "MC_CTF:weapon_x_mistake", "MC_CTF:wolverine_predator",
#         "MC_CTF:logan_hunter_killer", "MC_CTF:wolverine_torn_apart", "MC_CTF:logan_fought_apocalypse",
#         "MC_CTF:mutant_warrior", "MC_CTF:logan_last_stand", "MC_CTF:snikt_six_hundred_times",
#         "MC_CTF:wolverine_slashes", "MC_CTF:logan_doesnt_fall", "MC_CTF:weapon_x_failure",
#         "MC_CTF:wolverine_vs_hydra", "MC_CTF:logan_does_not_break", "MC_CTF:claws_of_rage",
#         "MC_CTF:wolverine_vs_vampires", "MC_CTF:logan_still_alive", "MC_CTF:wolverine_vs_doom",
#         "MC_CTF:logan_wins_always", "MC_CTF:adamantium_armor", "MC_CTF:wolverine_vs_hulk",
#         "MC_CTF:logan_is_revenge", "MC_CTF:berserker_slash", "MC_CTF:logan_toughest_mutant",
#         "MC_CTF:snikt_sharpest_claws", "MC_CTF:logan_vs_aliens", "MC_CTF:wolverine_vs_taskmaster",
#         "MC_CTF:logan_warrior_legend", "MC_CTF:wolverine_does_not_surrender", "MC_CTF:logan_vs_phoenix",
#         "MC_CTF:wolverine_vs_ghost_rider", "MC_CTF:wolverine_ripped_apart", "MC_CTF:logan_destroys_all",
#         "MC_CTF:adamantium_knuckles", "MC_CTF:wolverine_tracked_down", "MC_CTF:logan_vs_super_skrulls",
#         "MC_CTF:logan_never_quits", "MC_CTF:mutant_executioner", "MC_CTF:logan_vs_sentinels_final_battle",
#         "MC_CTF:wolverine_pierces_skulls", "MC_CTF:wolverine_bloodied", "MC_CTF:logan_came_back_again",
#         "MC_CTF:wolverine_vs_dark_phoenix", "MC_CTF:logan_is_xmen", "MC_CTF:wolverine_vs_everyone",
#         "MC_CTF:MC_CTF_really?", "MC_CTF:are_you_a_fool", "MC_CTF:you_thought_this_was_easy",
#         "MC_CTF:this_is_not_the_flag", "MC_CTF:did_you_really_try_this", "MC_CTF:bruh_try_harder",
#         "MC_CTF:seriously_not_the_flag", "MC_CTF:fake_flag_404", "MC_CTF:better_luck_next_time",
#         "MC_CTF:not_even_close", "MC_CTF:did_you_just_copy_paste"
#     ]

#     encoded_flags = {flag: encode_flag(flag) for flag in flags}

#     for original, encoded in encoded_flags.items():
#         print(f"{encoded}")

# if __name__ == "__main__":
#     main()
import base64

def encode_flag(flag, times=15):
    encoded = flag.encode()
    for _ in range(times):
        encoded = base64.b64encode(encoded)
    return encoded.decode()

def main():
    flags = [
        "MC_CTF:adamantium_wrath", "MC_CTF:logan_fury", "MC_CTF:berserker_mode",
        "MC_CTF:weapon_x_project", "MC_CTF:xmen_resistance", "MC_CTF:wolverine_warrior",
        "MC_CTF:claws_unleashed", "MC_CTF:logan_survivor", "MC_CTF:feral_instincts",
        "MC_CTF:wild_hunter_x", "MC_CTF:rage_within", "MC_CTF:canadian_beast",
        "MC_CTF:team_x_escape", "MC_CTF:snikt_master", "MC_CTF:mutant_avenger",
        "MC_CTF:logan_vs_sentinels", "MC_CTF:healing_factor_x", "MC_CTF:adamantium_blood",
        "MC_CTF:logan_unbreakable", "MC_CTF:dark_wolverine", "MC_CTF:wolverine_xforce",
        "MC_CTF:logan_shadow", "MC_CTF:wolverine_vs_omega_red", "MC_CTF:mutant_mercenary",
        "MC_CTF:wolverine_experiment", "MC_CTF:logan_battlefield", "MC_CTF:clawed_through_time",
        "MC_CTF:regeneration_overdrive", "MC_CTF:snikt_in_the_night", "MC_CTF:logan_vs_ninjas",
        "MC_CTF:ultimate_wolverine", "MC_CTF:xmen_legends", "MC_CTF:wolverine_inferno",
        "MC_CTF:logan_no_memory", "MC_CTF:beast_mode_snikt", "MC_CTF:weapon_x_initiative",
        "MC_CTF:logan_ghost", "MC_CTF:wolverine_lone_warrior", "MC_CTF:xmen_berserker",
        "MC_CTF:logan_never_forgets", "MC_CTF:wolverine_vs_sabretooth", "MC_CTF:logan_hunter",
        "MC_CTF:mutant_assassin_x", "MC_CTF:logan_tactical", "MC_CTF:adamantium_tiger",
        "MC_CTF:xmen_blacklist", "MC_CTF:logan_resurrection", "MC_CTF:wolverine_vs_deadpool",
        "MC_CTF:Adamantium_Unbreakable_But_You_Aren't",
        "MC_CTF:mutant_rage", "MC_CTF:logan_fangs", "MC_CTF:wolverine_immortal",
        "MC_CTF:logan_samurai", "MC_CTF:logan_alpha_flight", "MC_CTF:adamantium_wound",
        "MC_CTF:logan_fury_unleashed", "MC_CTF:weapon_x_mistake", "MC_CTF:wolverine_predator",
        "MC_CTF:logan_hunter_killer", "MC_CTF:wolverine_torn_apart", "MC_CTF:logan_fought_apocalypse",
        "MC_CTF:mutant_warrior", "MC_CTF:logan_last_stand", "MC_CTF:snikt_six_hundred_times",
        "MC_CTF:wolverine_slashes", "MC_CTF:logan_doesnt_fall", "MC_CTF:weapon_x_failure",
        "MC_CTF:wolverine_vs_hydra", "MC_CTF:logan_does_not_break", "MC_CTF:claws_of_rage",
        "MC_CTF:wolverine_vs_vampires", "MC_CTF:logan_still_alive", "MC_CTF:wolverine_vs_doom",
        "MC_CTF:logan_wins_always", "MC_CTF:adamantium_armor", "MC_CTF:wolverine_vs_hulk",
        "MC_CTF:logan_is_revenge", "MC_CTF:berserker_slash", "MC_CTF:logan_toughest_mutant",
        "MC_CTF:snikt_sharpest_claws", "MC_CTF:logan_vs_aliens", "MC_CTF:wolverine_vs_taskmaster",
        "MC_CTF:logan_warrior_legend", "MC_CTF:wolverine_does_not_surrender", "MC_CTF:logan_vs_phoenix",
        "MC_CTF:wolverine_vs_ghost_rider", "MC_CTF:wolverine_ripped_apart", "MC_CTF:logan_destroys_all",
        "MC_CTF:adamantium_knuckles", "MC_CTF:wolverine_tracked_down", "MC_CTF:logan_vs_super_skrulls",
        "MC_CTF:logan_never_quits", "MC_CTF:mutant_executioner", "MC_CTF:logan_vs_sentinels_final_battle",
        "MC_CTF:wolverine_pierces_skulls", "MC_CTF:wolverine_bloodied", "MC_CTF:logan_came_back_again",
        "MC_CTF:wolverine_vs_dark_phoenix", "MC_CTF:logan_is_xmen", "MC_CTF:wolverine_vs_everyone",
        "MC_CTF:MC_CTF_really?", "MC_CTF:are_you_a_fool", "MC_CTF:you_thought_this_was_easy",
        "MC_CTF:this_is_not_the_flag", "MC_CTF:did_you_really_try_this", "MC_CTF:bruh_try_harder",
        "MC_CTF:seriously_not_the_flag", "MC_CTF:fake_flag_404", "MC_CTF:better_luck_next_time",
        "MC_CTF:not_even_close", "MC_CTF:did_you_just_copy_paste"
    ]

    encoded_flags = {flag: encode_flag(flag) for flag in flags}

    with open("encoded_flags.txt", "w") as file:
        for original, encoded in encoded_flags.items():
            file.write(f"{encoded}\n")

if __name__ == "__main__":
    main()
