from math import floor
import variables

def calc_speed(speed, condition):
    if condition == "最速":
        val = ((speed*2+31+252/4)*0.5+5)*1.1
    elif condition == "準速":
        val = (speed*2+31+252/4)*0.5+5
    elif condition == "無振り":
        val = (speed*2+31)*0.5+5
    elif condition in ["下降", "最遅"]:
        val = ((speed*2+31)*0.5+5)*0.9
    else:
        return 0

    return floor(val)

def resolve_pokemon_name(name, option, base_dict):
    if name in variables.MEGA_MAP:
        if option in variables.MEGA_MAP[name]:
            return variables.MEGA_MAP[name][option]

    if name in variables.FORM_MAP:
        if option in variables.FORM_MAP[name]:
            return variables.FORM_MAP[name][option]

    return base_dict.get(name)

def get_dict_id_of_pokemon():
    result = {}
    with open("ja_2_id.txt", encoding="utf-8") as f:
        for line in f:
            ja, en = line.strip().split("\t")
            result[ja] = en
    return result