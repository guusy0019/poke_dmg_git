from ..models import PokeModel, PokeMove

def choice_atk_def(request):
    #攻撃側のポケモンと攻撃技を取得
    name1 = request.POST.get('name1')  
    poke_atk = PokeModel.objects.get(poke_name=name1)
    poke_move = request.POST.get('poke_move')
    poke_move = PokeMove.objects.get(move_name=poke_move)

    #防御側のポケモンを取得
    name2 = request.POST.get('name2')
    poke_def = PokeModel.objects.get(poke_name=name2)
    #天候で補正値を適合するためにタプル型でタイプを取得
    poke_types = poke_def.poke_type, poke_def.poke_type2
    #天候を取得
    poke_env = request.POST.get('poke_env')

    if poke_move.move_class == 'physical':
        #種族値を取得
        atk_nums = poke_atk.poke_attack
        #個体値を取得、値がない場合31
        atk_ivs = request.POST.get('atk_iv', '31')
        #努力値を取得
        atk_evs = request.POST.get('atk_ev', '0')
        #レベルを取得
        atk_levels = request.POST.get('atk_level', '50')
        #性格補正を取得
        atk_natures = request.POST.get('atk_nature', '1')
        #攻撃側のステータスを計算
        atk_status = int(atk_nums) * 2 + int(atk_ivs) + int(atk_evs) / 4 * int(atk_levels) / 100 + 5 * float(atk_natures)
        #攻撃技の威力を取得
        poke_moves = poke_move.move_power
        
        #防御側のステータスを計算
        #天候が雪の場合の補正値を取得
        if poke_env == 'ゆき' and 'こおり' in poke_types:
            def_nums = poke_def.poke_defense
            def_nums *= 1.5
            def_ivs = request.POST.get('def_iv', '31')
            def_evs = request.POST.get('def_ev', '0')
            def_levels = request.POST.get('def_level', '50')
            def_natures = request.POST.get('def_nature', '1')
            def_status = int(def_nums) * 2 + int(def_ivs) + int(def_evs) / 4 * int(def_levels) / 100 + 5 * float(def_natures)
            #最後の計算
            choice_result = poke_moves * atk_status / def_status
            return choice_result
        else:
            def_nums = poke_def.poke_defense
            def_ivs = request.POST.get('def_iv', '31')
            def_evs = request.POST.get('def_ev', '0')
            def_levels = request.POST.get('def_level', '50')
            def_natures = request.POST.get('def_nature', '1')
            def_status = int(def_nums) * 2 + int(def_ivs) + int(def_evs) / 4 * int(def_levels) / 100 + 5 * float(def_natures)
            #最後の計算
            choice_result = poke_moves * atk_status / def_status
            return choice_result
    
    #特攻の時の場合
    #天候が砂嵐の場合の補正値を記述
    elif poke_move.move_class == 'special':
        #攻撃側のステータスを取得
        atk_nums = poke_atk.poke_sp_atk
        atk_ivs = request.POST.get('atk_iv', '31')
        atk_evs = request.POST.get('atk_ev', '0')
        atk_levels = request.POST.get('atk_level', '50')
        atk_natures = request.POST.get('atk_nature', '1')
        atk_status = int(atk_nums) * 2 + int(atk_ivs) + int(atk_evs) / 4 * int(atk_levels) / 100 + 5 * float(atk_natures)
        poke_moves = poke_move.move_power

        #防御側のステータスを計算
        if poke_env == 'すなあらし' and 'いわ' in poke_types:
            def_nums = poke_def.poke_sp_def
            def_nums *= 1.5
            def_ivs = request.POST.get('def_iv', '31')
            def_evs = request.POST.get('def_ev', '0')
            def_levels = request.POST.get('def_level', '50')
            def_natures = request.POST.get('def_nature', '1')
            def_status = int(def_nums) * 2 + int(def_ivs) + int(def_evs) / 4 * int(def_levels) / 100 + 5 * float(def_natures)
            #最後の計算
            choice_result = poke_moves * atk_status / def_status
            return choice_result
        else:
            def_nums = poke_def.poke_sp_def
            def_ivs = request.POST.get('def_iv', '31')
            def_evs = request.POST.get('def_ev', '0')
            def_levels = request.POST.get('def_level', '50')
            def_natures = request.POST.get('def_nature', '1')
            def_status = int(def_nums) * 2 + int(def_ivs) + int(def_evs) / 4 * int(def_levels) / 100 + 5 * float(def_natures)
            #最後の計算
            choice_result = poke_moves * atk_status / def_status
            return choice_result
    
    #おそらくだが変化技の場合は変化しないので１でいい
    return 1

#天気補正関数
#晴れなら炎タイプの技が1.5倍、水タイプの技は半減
#雨なら水タイプの技が1.5倍、炎タイプの技が半減
def weather_effects(request):
    #攻撃側のポケモンと攻撃技を取得 
    poke_move = request.POST.get('poke_move')
    poke_move = PokeMove.objects.get(move_name=poke_move)
    move_types = poke_move.move_type
    #天候を取得
    poke_env = request.POST.get('poke_env')

    weather_effects_nums = 1
    if move_types == 'ほのお' and poke_env == 'はれ':
        weather_effects_nums = 1.5
        return weather_effects_nums
    
    elif move_types == 'みず' and poke_env == 'あめ':
        weather_effects_nums = 1.5
        return weather_effects_nums
    
    return weather_effects_nums


#タイプ一致補正関数
def type_match_bounus(request):
    tera_types = request.POST.get('atk_tera_type')
    name1 = request.POST.get('name1')  
    poke_atk = PokeModel.objects.get(poke_name=name1)
    poke_types = poke_atk.poke_type, poke_atk.poke_type2
    poke_abilitys = poke_atk.poke_ability, poke_atk.poke_ability2, poke_atk.poke_abi_hidden

    poke_move = request.POST.get('poke_move')
    poke_move = PokeMove.objects.get(move_name=poke_move)
    move_types = poke_move.move_type
    
    type_match_bounus_nums = 1
    #テラスタルなしの場合
    if tera_types == 'なし':
        if move_types in poke_types and 'てきおうりょく' not in poke_abilitys:
            type_match_bounus_nums = 1.5
            return type_match_bounus_nums
        
        elif move_types in poke_types and 'てきおうりょく' in poke_abilitys:
            type_match_bounus_nums = 2
            return type_match_bounus_nums

        return type_match_bounus_nums
    
    #テラスタルありの場合
    elif tera_types != 'なし':
        if tera_types not in poke_types and tera_types == move_types and 'てきおうりょく' not in poke_abilitys:
            type_match_bounus_nums = 1.5
            return type_match_bounus_nums

        elif tera_types not in poke_types and tera_types == move_types and 'てきおうりょく' in poke_abilitys:
            type_match_bounus_nums = 2
            return type_match_bounus_nums
        
        elif tera_types in poke_types and tera_types == move_types and 'てきおうりょく' not in poke_abilitys:
            type_match_bounus_nums = 2
            return type_match_bounus_nums

        elif tera_types in poke_types and tera_types == move_types and 'てきおうりょく' in poke_abilitys:
            type_match_bounus_nums = 2.25
            return type_match_bounus_nums
        
        elif move_types in poke_types and tera_types not in poke_types and 'てきおうりょく' in poke_abilitys:
            type_match_bounus_nums = 1.5
            return type_match_bounus_nums
        
        elif move_types in poke_types and tera_types not in poke_types and 'てきおうりょく' not in poke_abilitys:
            type_match_bounus_nums = 1.5
            return type_match_bounus_nums
    
    return type_match_bounus_nums


#chatGPT answer
def calculate_damage(move, attacker, defender, is_critical):
    # 通常のダメージ計算を行います。
    base_damage = calculate_base_damage(move, attacker, defender)
    
    # 壁補正、ランク補正を計算します。
    wall_modifier = calculate_wall_modifier(defender)
    attack_rank_modifier = calculate_rank_modifier(attacker, "attack")
    defense_rank_modifier = calculate_rank_modifier(defender, "defense")
    
    # 急所かどうかで処理を分けます。
    if is_critical:
        # 急所の場合、補正を無視してダメージを返します。
        return base_damage
    else:
        # 急所でない場合、全ての補正を適用してダメージを返します。
        return base_damage * wall_modifier * attack_rank_modifier * defense_rank_modifier

# この関数の中で、実際の基本ダメージ、壁補正、ランク補正の計算を行います。
# これらはポケモンのステータス、使用する技、壁の有無、ランクの状態によります。
def calculate_base_damage(move, attacker, defender):
    pass  # 実装する

def calculate_wall_modifier(defender):
    pass  # 実装する

def calculate_rank_modifier(pokemon, stat):
    pass  # 実装する



#攻撃なら防御で、特攻なら特防で計算して（攻撃技の威力✖️攻撃側÷防御側）の計算をしてくれる関数
def choice_atk_def(request,
                   poke_atk, 
                   poke_move, 
                   poke_move_class,
                   poke_def,
                   atk_poke_types,
                   poke_env,
                   atk_nums,
                   atk_sp_nums,
                   atk_ivs,
                   atk_evs,
                   atk_levels,
                   atk_natures,
                   atk_status,
                   move_powers,
                   def_nums,
                   def_sp_nums,
                   def_ivs,
                   def_evs,
                   def_levels,
                   def_natures,
                   def_status,
                   ):

    if poke_move_class == 'physical':
        #攻撃側のステータスを計算
        atk_status = int(atk_nums) * 2 + int(atk_ivs) + int(atk_evs) / 4 * int(atk_levels) / 100 + 5 * float(atk_natures)
        #攻撃技の威力を取得
        poke_moves = poke_move.move_power
        
        #防御側のステータスを計算
        #天候が雪の場合の補正値を取得
        if poke_env == 'ゆき' and 'こおり' in atk_poke_types:
            def_nums *= 1.5
            def_status = int(def_nums) * 2 + int(def_ivs) + int(def_evs) / 4 * int(def_levels) / 100 + 5 * float(def_natures)
            #最後の計算
            choice_result = poke_moves * atk_status / def_status
            return choice_result
        else:
            def_status = int(def_nums) * 2 + int(def_ivs) + int(def_evs) / 4 * int(def_levels) / 100 + 5 * float(def_natures)
            #最後の計算
            choice_result = poke_moves * atk_status / def_status
            return choice_result
    
    #特攻の時の場合
    #天候が砂嵐の場合の補正値を記述
    elif poke_move_class == 'special':
        #攻撃側のステータスを取得
        atk_status = int(atk_sp_nums) * 2 + int(atk_ivs) + int(atk_evs) / 4 * int(atk_levels) / 100 + 5 * float(atk_natures)
        poke_moves = poke_move.move_power

        #防御側のステータスを計算
        if poke_env == 'すなあらし' and 'いわ' in atk_poke_types:
            def_sp_nums *= 1.5
            def_status = int(def_sp_nums) * 2 + int(def_ivs) + int(def_evs) / 4 * int(def_levels) / 100 + 5 * float(def_natures)
            #最後の計算
            choice_result = poke_moves * atk_status / def_status
            return choice_result
        else:
            def_status = int(def_sp_nums) * 2 + int(def_ivs) + int(def_evs) / 4 * int(def_levels) / 100 + 5 * float(def_natures)
            #最後の計算
            choice_result = poke_moves * atk_status / def_status
            return choice_result
    
    #おそらくだが変化技の場合は変化しないので１でいい
    return 1
