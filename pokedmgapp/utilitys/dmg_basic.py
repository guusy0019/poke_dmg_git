from ..models import PokeModel, PokeMove

# ダメージ=攻撃側のレベル×2÷5+2→切り捨て
# 　×物理技(特殊技)の威力×攻撃側のこうげき(とくこう)÷防御側のぼうぎょ(とくぼう)→切り捨て
# 　÷50+2→切り捨て
# 　×乱数(0.85, 0.86, …… ,0.99, 1.00 の何れか)→切り捨て


# HP
# {(種族値×2＋個体値＋努力値/4)×Lv/100}＋10＋Lv


# 攻撃,防御,特攻,特防,素早さ
# [{(種族値×2＋個体値＋努力値/4)×Lv/100}＋5]×性格補正(1.1,1.0,0.9)

#防御側のポケモンのHPを計算
def calc_def_poke_hp(request, base_hp, int_def_iv, int_def_ev, int_def_level):
    def_poke_hp = (base_hp * 2 + int_def_iv + int_def_ev / 4) * int_def_level / 100 
    def_poke_hp_result = def_poke_hp + 10 + int_def_level
    return def_poke_hp_result

def calc_poke_status(
                     base_a, 
                     base_b, 
                     base_c, 
                     base_d, 
                     atk_ev, 
                     atk_iv, 
                     def_ev,
                     def_iv,
                     atk_rank_num,
                     def_rank_num,
                     atk_level,
                     def_level,
                     poke_move_class, 
                     atk_nature, 
                     def_nature
                     ):
    #numはそのポケモンのステータス、resultはランクを考慮した値
    #atk_nature or def_narureの引数がNoneだとエラーがでてしますため、処理を分岐
    if atk_nature is None or def_nature is None:
        if poke_move_class == 'physical':
            a_num = (((base_a * 2 + atk_iv + atk_ev / 4) * atk_level / 100) + 5)
            a_result = a_num * atk_rank_num
            
            b_num = (((base_b * 2 + def_iv + def_ev / 4) * def_level / 100) + 5)
            b_result = b_num * def_rank_num

            c_num = ((base_c * 2 / 4) * atk_level / 100) + 5
            c_result = c_num

            d_num = ((base_d * 2 / 4) * def_level / 100) + 5
            d_result = d_num

            return {'a_num': a_num, 
                    'a_result': a_result, 
                    'b_num': b_num, 
                    'b_result': b_result,
                    'c_num': c_num,
                    'c_result': c_result,
                    'd_num': d_result,
                    'd_result': d_result,
                    }

        elif poke_move_class == 'special':
            c_num = (((base_c * 2 + atk_iv + atk_ev /4) * atk_level / 100) + 5 ) 
            c_result = c_num * atk_rank_num

            d_num = (((base_d * 2 + def_iv + def_ev / 4) * def_level / 100) + 5)
            d_result = d_num * def_rank_num

            a_num = ((base_a * 2 / 4) * atk_level / 100) + 5
            a_result = a_num

            b_num = ((base_b * 2 / 4) * def_level / 100) + 5
            b_result = b_num

            return {'a_num': a_num, 
                    'a_result': a_result, 
                    'b_num': b_num, 
                    'b_result': b_result,
                    'c_num': c_num,
                    'c_result': c_result,
                    'd_num': d_result,
                    'd_result': d_result,
                    }    

    if poke_move_class == 'physical':
        a_num = (((base_a * 2 + atk_iv + atk_ev / 4) * atk_level / 100) + 5) * atk_nature
        a_result = a_num * atk_rank_num
        
        b_num = (((base_b * 2 + def_iv + def_ev / 4) * def_level / 100) + 5) * def_nature
        b_result = b_num * def_rank_num

        c_num = ((base_c * 2 / 4) * atk_level / 100) + 5
        c_result = c_num

        d_num = ((base_d * 2 / 4) * def_level / 100) + 5
        d_result = d_num

        return {'a_num': a_num, 
                'a_result': a_result, 
                'b_num': b_num, 
                'b_result': b_result,
                'c_num': c_num,
                'c_result': c_result,
                'd_num': d_result,
                'd_result': d_result,
                }

    elif poke_move_class == 'special':
        c_num = (((base_c * 2 + atk_iv + atk_ev /4) * atk_level / 100) + 5 ) * atk_nature
        c_result = c_num * atk_rank_num

        d_num = (((base_d * 2 + def_iv + def_ev / 4) * def_level / 100) + 5) * def_nature
        d_result = d_num * def_rank_num

        a_num = ((base_a * 2 / 4) * atk_level / 100) + 5
        a_result = a_num

        b_num = ((base_b * 2 / 4) * def_level / 100) + 5
        b_result = b_num

        return {'a_num': a_num, 
                'a_result': a_result, 
                'b_num': b_num, 
                'b_result': b_result,
                'c_num': c_num,
                'c_result': c_result,
                'd_num': d_result,
                'd_result': d_result,
                }
    

#攻撃側のレベルを取得して計算
def calc_atk_levels(request, atk_level):
    atk_level_result = int(atk_level) * 2 / 5 + 2
    atk_level_result = round(atk_level_result)
    return atk_level_result

#×威力×A/D)部分の関数
#a_status_resultはランクアップを考慮
#防御のステータスが変わるので、ゆきとすなあらしの場合のステータスを考慮
def times_power_status(
                       a_status_result, 
                       b_status_result, 
                       c_status_result, 
                       d_status__result, 
                       move_powers, 
                       poke_move_class, 
                       poke_env,
                       def_poke_types
                       ):
    if poke_move_class == 'physical':
        if poke_env == 'ゆき' and 'こおり' in def_poke_types:
            b_status_result *= 1.5
            return move_powers * a_status_result / b_status_result
        else:
            return move_powers * a_status_result / b_status_result

    elif poke_move_class =='special':
        if poke_env == 'すなあらし' and 'いわ' in def_poke_types:
            d_status__result *= 1.5
            return move_powers * c_status_result / d_status__result
        else:
            return move_powers * c_status_result / d_status__result

    return 1      


#天気補正の関数
#晴れなら炎タイプの技が1.5倍、水タイプの技は半減
#雨なら水タイプの技が1.5倍、炎タイプの技が半減
def weather_effects(request, atk_move_types, poke_env):
    weather_effects_nums = 1
    if atk_move_types == 'ほのお' and poke_env == 'はれ':
        weather_effects_nums = 1.5
        return weather_effects_nums
    
    elif atk_move_types == 'みず' and poke_env == 'あめ':
        weather_effects_nums = 1.5
        return weather_effects_nums
    
    return weather_effects_nums


#タイプ一致補正関数
def type_match_bounus(request, atk_tera_type, poke_atk, atk_poke_types, atk_poke_abilitys, atk_move_types):
    type_match_bounus_nums = 1
    #テラスタルなしの場合
    if atk_tera_type == 'なし':
        if atk_move_types in atk_poke_types and 'てきおうりょく' not in atk_poke_abilitys:
            type_match_bounus_nums = 1.5
            return type_match_bounus_nums
        
        elif atk_move_types in atk_poke_types and 'てきおうりょく' in atk_poke_abilitys:
            type_match_bounus_nums = 2
            return type_match_bounus_nums

        return type_match_bounus_nums
    
    #テラスタルありの場合
    elif atk_tera_type != 'なし':
        if atk_tera_type not in atk_poke_types and atk_tera_type == atk_move_types and 'てきおうりょく' not in atk_poke_abilitys:
            type_match_bounus_nums = 1.5
            return type_match_bounus_nums

        elif atk_tera_type not in atk_poke_types and atk_tera_type == atk_move_types and 'てきおうりょく' in atk_poke_abilitys:
            type_match_bounus_nums = 2
            return type_match_bounus_nums
        
        elif atk_tera_type in atk_poke_types and atk_tera_type == atk_move_types and 'てきおうりょく' not in atk_poke_abilitys:
            type_match_bounus_nums = 2
            return type_match_bounus_nums

        elif atk_tera_type in atk_poke_types and atk_tera_type == atk_move_types and 'てきおうりょく' in atk_poke_abilitys:
            type_match_bounus_nums = 2.25
            return type_match_bounus_nums
        
        elif atk_move_types in atk_poke_types and atk_tera_type not in atk_poke_types and 'てきおうりょく' in atk_poke_abilitys:
            type_match_bounus_nums = 1.5
            return type_match_bounus_nums
        
        elif atk_move_types in atk_poke_types and atk_tera_type not in atk_poke_types and 'てきおうりょく' not in atk_poke_abilitys:
            type_match_bounus_nums = 1.5
            return type_match_bounus_nums
    
    return type_match_bounus_nums


#タイプ相性関数
def type_effectiveness(request, poke_move, atk_move_types, def_poke_types):
    #ここでdef_poke_typesはタプル型（不可変型）で値は絶対に存在する　why↓
    #ポケモンの名前の入力で誤りがある場合に既にエラーを発生させているため

    type_chart = {
    'ノーマル': {'いわ': 0.5, 'ゴースト': 0, 'はがね': 0.5},
    'ほのお': {'ほのお': 0.5, 'みず': 0.5, 'くさ': 2, 'こおり': 2, 'むし': 2, 'いわ': 0.5, 'ドラゴン': 0.5, 'はがね': 2},
    'みず': {'ほのお': 2, 'みず': 0.5, 'くさ': 0.5, 'じめん': 2, 'いわ': 2, 'ドラゴン': 0.5},
    'でんき': {'みず': 2, 'でんき': 0.5, 'くさ': 0.5, 'じめん': 0, 'ひこう': 2, 'ドラゴン': 0.5},
    'くさ': {'ほのお': 0.5, 'みず': 2, 'くさ': 0.5, 'どく': 0.5, 'じめん': 2, 'ひこう': 0.5, 'むし': 0.5, 'いわ': 2, 'ドラゴン': 0.5, 'はがね': 0.5},
    'こおり': {'ほのお': 0.5, 'みず': 0.5, 'くさ': 2, 'こおり': 0.5, 'じめん': 2, 'ひこう': 2, 'ドラゴン': 2, 'はがね': 0.5},
    'かくとう': {'ノーマル': 2, 'こおり': 2, 'どく': 0.5, 'ひこう': 0.5, 'エスパー': 0.5, 'むし': 0.5, 'いわ': 2, 'ゴースト': 0, 'あく': 2, 'はがね': 2, 'フェアリー': 0.5},
    'どく': {'くさ': 2, 'じめん': 0.5, 'いわ': 0.5, 'ゴースト': 0.5, 'はがね': 0, 'フェアリー': 2},
    'じめん': {'ほのお': 2, 'でんき': 2, 'くさ': 0.5, 'どく': 2, 'ひこう': 0, 'むし': 0.5, 'いわ': 2, 'はがね': 2},
    'ひこう': {'でんき': 0.5, 'くさ': 2, 'かくとう': 2, 'むし': 2, 'いわ': 0.5, 'はがね': 0.5},
    'エスパー': {'かくとう': 2, 'どく': 2, 'ゴースト': 1, 'エスパー': 0.5, 'あく': 0, 'はがね': 0.5},
    'むし': {'ほのお': 0.5, 'くさ': 2, 'かくとう': 0.5, 'どく': 0.5, 'ひこう': 0.5, 'エスパー': 2, 'ゴースト': 0.5, 'あく': 2, 'はがね': 0.5, 'フェアリー': 0.5},
    'いわ': {'ほのお': 2, 'こおり': 2, 'かくとう': 0.5, 'じめん': 0.5, 'ひこう': 2, 'むし': 2, 'はがね': 0.5},
    'ゴースト': {'ノーマル': 0, 'エスパー': 2, 'ゴースト': 2, 'あく': 0.5},
    'ドラゴン': {'ドラゴン': 2, 'はがね': 0.5, 'フェアリー': 0},
    'あく': {'かくとう': 0.5, 'エスパー': 2, 'ゴースト': 2, 'あく': 0.5, 'フェアリー': 0.5},
    'はがね': {'ほのお': 0.5, 'みず': 0.5, 'でんき': 0.5, 'こおり': 2, 'いわ': 2, 'はがね': 0.5, 'フェアリー': 2},
    'フェアリー': {'ほのお': 0.5, 'かくとう': 2, 'どく': 0.5, 'ドラゴン': 2, 'あく': 2, 'はがね': 0.5}
    }
    
    #type_chart[atk_move_types]は辞書の辞書の情報を取得している
    effectiveness1 = type_chart[atk_move_types].get(def_poke_types[0], 1)
    effectiveness2 = type_chart[atk_move_types].get(def_poke_types[1], 1) if def_poke_types[1] else 1
    total_effectiveness = effectiveness1 * effectiveness2

    return total_effectiveness

    

#やけど補正の関数
#引数にやけど状態の有無と攻撃の種類（物理か特殊かを受け取る）
#攻撃技がからげんきの場合やけど状態でも１（変化しない）を返す
#atk_situは複数個ある
def burn_correction(request, atk_situ, poke_move_kinds, move_name):
    burn_correction_num = 1
    if 'atk_burn' in atk_situ and poke_move_kinds == 'physical':
        burn_correction_num *= 0.5
        return burn_correction_num
    
    elif 'atk_burn' in atk_situ and poke_move_kinds == 'physical' and move_name == 'からげんき':
        return burn_correction_num
    
    else:
        return burn_correction_num
    


