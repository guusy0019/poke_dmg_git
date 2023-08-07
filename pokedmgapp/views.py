from django.shortcuts import render
from .models import PokeModel, PokeMove
from .utilitys.itemfunc import atk_itemfunc, def_itemfunc
from .utilitys.dmg_basic import (
    calc_atk_levels, 
    calc_poke_status,
    times_power_status,
    weather_effects, 
    type_match_bounus, 
    type_effectiveness, 
    burn_correction,
    calc_def_poke_hp,
)
from .utilitys.dmg_m_etc import (
    wall_correct,
)

from .utilitys.change_rank_num import(change_atk_rank_num, change_def_rank_num)
from.utilitys.round_off_func import(round_4_5, round_5_5, round_up)
# Create your views here.
#ポケモンdmgを表示させるための関数
def pokedmgfunc(request):
    object_list = PokeModel.objects.all()
    return render(request, 'pokedmg.html', {'object_list': object_list})

def pokedmgfunc2(request):
    if request.method =="POST":
        # フォームから送信されたポケモン名を取得
        #　name1は攻撃側、name2は防御側
        name1 = request.POST.get('name1')  
        name2 = request.POST.get('name2')
        poke_move = request.POST.get('poke_move')

        try:
            # モデル内のポケモン名と照合（攻撃側）してポケモンを取得
            poke_atk = PokeModel.objects.get(poke_name=name1)

            #攻撃側のテラスタイプを取得
            #テラスタルはゲットリクエストで空白だった場合値は''になる
            atk_tera_type = request.POST.get('atk_tera_type')
            
            #攻撃技を取得
            poke_move = PokeMove.objects.get(move_name=poke_move)
            
            #攻撃側の努力値を取得
            atk_ev = request.POST.get('atk_ev')

            #攻撃側の個体値を取得
            atk_iv = request.POST.get('atk_iv')

            #攻撃側の攻撃ランクを取得
            atk_rank = request.POST.get('atk_rank')

            #攻撃側の特性を取得
            atk_abi = request.POST.get('atk_abi')

            #攻撃側のレベルを指定
            atk_level = request.POST.get('atk_level')

            #攻撃側のもちものを取得する,倍率の数字型で変数に代入
            atk_item = request.POST.get('atk_item')   

            #攻撃側の性格補正を取得する
            atk_nature = request.POST.get('atk_nature')

            #攻撃側から各チェックポイントを受け取る
            atk_situ = request.POST.getlist('atk_situ')

            #____________________________
            # モデル内のポケモン名と照合（防御側） 
            poke_def = PokeModel.objects.get(poke_name=name2)

            #防御側のテラスタイプを取得
            def_tera_type = request.POST.get('def_tera_type')
            def_level = request.POST.get('def_level')

            #防御側のB努力値を取得
            def_ev = request.POST.get('def_ev')

            #防御側のBの個体値を取得
            def_iv = request.POST.get('def_iv')

            #防御側のH努力値を取得
            def_hp = request.POST.get('def_hp')

            #防御側のHの個体値を取得
            def_iv_hp = request.POST.get('def_iv_hp')

            #防御側の攻撃ランクを取得
            def_rank = request.POST.get('def_rank')

            #防御側の特性を取得
            def_abi = request.POST.get('def_abi')

            #防御側のもちものを取得する,倍率の数字型で変数に代入
            def_item = request.POST.get('def_item')

            #防御側の性格補正を取得する
            def_nature = request.POST.get('def_nature')

            #防御側から各チェックポイントを受け取る
            def_situ = request.POST.getlist('def_situ')

            #環境その他の情報を取得
            poke_env = request.POST.get('poke_env')

            #フィールド情報を取得
            poke_fild = request.POST.get('poke_fild')

            #災系情報の取得
            poke_etc = request.POST.get('poke_etc')

            #追加ダメージ情報を取得
            add_dmg = request.POST.get('add_dmg')
            
            
            #_________________________
            #ポケモンのダメージ計算式
            #ダメージ = (((レベル×2/5+2)×威力×A/D)/50+2)
            # ×範囲補正×おやこあい補正×天気補正×急所補正
            # ×乱数補正×タイプ一致補正×相性補正×やけど補正×M×Mprotect


            # HP
            # {(種族値×2＋個体値＋努力値/4)×Lv/100}＋10＋Lv


            # 攻撃,防御,特攻,特防,素早さ
            # [{(種族値×2＋個体値＋努力値/4)×Lv/100}＋5]×性格補正(1.1,1.0,0.9)

            #atk_rankとdef_rankを計算できる形にして取り出す関数
            atk_rank_num = change_atk_rank_num(atk_rank)
            def_rank_num = change_def_rank_num(def_rank)



            #ポケモンのHPを正数で求める関数
            #防御側のポケモンのHPの種族値をbase_hp
            base_hp = poke_def.poke_hp
            int_def_iv = int(def_iv_hp)
            int_def_ev = int(def_hp)
            int_def_level = int(def_level)
            def_poke_hp = calc_def_poke_hp(request, base_hp, int_def_iv, int_def_ev, int_def_level)
            print(f'防御側のポケモンのHP {def_poke_hp}')

            #ポケモンのH以外の数値を求める関数
            #なおランクを考慮する
            #攻撃側の技の種類、物理か特殊かを取得
            poke_move_class = poke_move.move_class
            base_a = poke_atk.poke_attack
            base_b = poke_def.poke_defense
            base_c = poke_atk.poke_sp_atk
            base_d = poke_atk.poke_sp_def
            int_atk_iv = int(atk_iv)
            int_atk_ev = int(atk_ev)  
            int_def_iv = int(def_iv)          
            int_def_ev = int(def_ev)
            int_atk_level = int(atk_level)
            float_atk_nature = float(atk_nature)
            float_def_nature = float(def_nature)

            poke_status_dict = calc_poke_status(
                                           base_a, 
                                           base_b, 
                                           base_c, 
                                           base_d, 
                                           int_atk_ev, 
                                           int_atk_iv,
                                           int_def_ev,
                                           int_def_iv,
                                           atk_rank_num,
                                           def_rank_num,
                                           int_atk_level,
                                           int_def_level,
                                           poke_move_class, 
                                           float_atk_nature, 
                                           float_def_nature,
                                           )
            a_status = poke_status_dict['a_num']   
            a_status_result = poke_status_dict['a_result']

            b_status = poke_status_dict['b_num']
            b_status_result = poke_status_dict['b_result']

            c_status = poke_status_dict['c_num']
            c_status_result = poke_status_dict['c_result']

            d_status = poke_status_dict['d_num']
            d_status__result = poke_status_dict['d_result']

            print(f'Aのステータスは{a_status}です')
            print(f'Aの実際のステータスは{a_status_result}です')

            
            #攻撃側のレベルの部分の数値を取得
            poke_atk_level = calc_atk_levels(request, atk_level)
            poke_atk_level = int(poke_atk_level)
            print(f'(レベル✖️2/5+2)の関数:{poke_atk_level}')


            #攻撃技の威力を取得
            move_powers = poke_move.move_power
            #防御側のタイプを取得
            def_poke_types = poke_def.poke_type, poke_def.poke_type2

            #×威力×A/D 部分の関数
            #move_powers_は技の威力
            poke_times_status = times_power_status(
                                                   a_status_result, 
                                                   b_status_result, 
                                                   c_status_result, 
                                                   d_status__result, 
                                                   move_powers, 
                                                   poke_move_class, 
                                                   poke_env,
                                                   def_poke_types,
                                                   )
            poke_times_status = int(poke_times_status)
            print(f'威力×A/Dは {poke_times_status}')

            #ダメージ = (((レベル×2/5+2)×威力×A/D)/50+2)
            #上記のレベル関数とBならBで関数で上の部分を完成させる
            level_and_status_dmg = int(poke_atk_level * poke_times_status / 50 + 2)
            print(f'(((レベル×2/5+2)×威力×A/D)/50+2): {level_and_status_dmg}')

            #天気補正の関数を取得
            move_types = poke_move.move_type
            poke_weather_effeects = weather_effects(request, move_types, poke_env)
            poke_weather_effeects = round_5_5(poke_weather_effeects)
            print('天気補正関数:' + str(poke_weather_effeects))

            #タイプ一致補正（テラスタルも込み）を取得
            #てきおうりょくをしらべるために特性も変数に代入
            atk_poke_types = poke_atk.poke_type, poke_atk.poke_type2
            atk_poke_abilitys = poke_atk.poke_ability, poke_atk.poke_ability2, poke_atk.poke_abi_hidden
            atk_move_types = poke_move.move_type

            poke_type_match_bonus = type_match_bounus(request, atk_tera_type, poke_atk, atk_poke_types, atk_poke_abilitys, atk_move_types)
            print(f'タイプ一致補正関数:{poke_type_match_bonus}')

            #タイプ相性を取得
            poke_effectiveness = type_effectiveness(request, poke_move, atk_move_types, def_poke_types)
            print(f'相性関数 {poke_effectiveness}')

            #やけど補正を取得
            #やけど状態の有無を取得
            #攻撃技の種類（物理か特殊）を取得
            #からげんきを判断するため技名を取得
            poke_move_kinds = poke_move.move_class
            move_name_kara = poke_move.move_name
            poke_burn_corrction = burn_correction(request, atk_situ, poke_move_kinds, move_name_kara)
            print(f'やけど補正関数 {poke_burn_corrction}')

            #________________
            #    以下M部分の関数を記述
            #M→     #  M=壁補正×ブレインフォース補正×スナイパー補正×いろめがね補正
                    #  ×もふもふほのお補正×Mhalf×Mfilter×フレンドガード補正×たつじんのおび補正
                    #  ×メトロノーム補正×いのちのたま補正×半減の実補正×Mtwice
            #poke_move_kindsは物理か特殊か変化技か
            poke_wall = request.POST.get('def_situ')
            poke_wall_correcttion = wall_correct(request, poke_wall, poke_move_kinds)
            print(f'壁補正関数 {poke_wall_correcttion}')


            #________________
            #   最終ダメージを計算
            #   ダメージ = (((レベル×2/5+2)×威力×A/D)/50+2)×範囲補正
            #   ×おやこあい補正×天気補正×急所補正×乱数補正×タイプ一致補正
            #   ×相性補正×やけど補正×M×Mprotect

            min_final_dmg = level_and_status_dmg * poke_weather_effeects \
            * poke_type_match_bonus * poke_effectiveness * poke_burn_corrction \
            * 85 / 100

            max_final_dmg = level_and_status_dmg * poke_weather_effeects \
            * poke_type_match_bonus * poke_effectiveness * poke_burn_corrction \

            min_final_dmg = int(min_final_dmg)
            max_final_dmg = int(max_final_dmg)        

            print(f'最小ダメージ {min_final_dmg}')
            print(f'最大ダメージ {max_final_dmg}')

            percent_min_final_dmg = min_final_dmg / def_poke_hp * 100
            percent_max_final_dmg = max_final_dmg / def_poke_hp * 100
            percent_min_final_dmg = int(percent_min_final_dmg)
            percent_max_final_dmg = int(percent_max_final_dmg)
            percent_for_width = 100 - percent_max_final_dmg
            print(f'最小ダメージの%は {percent_min_final_dmg}')
            print(f'最大ダメージの%は {percent_max_final_dmg}')

            


            
            context = {
                #攻撃側の情報
                'poke_atk': poke_atk, 
                'atk_tera_type':atk_tera_type,
                'poke_move': poke_move,
                'atk_ev': atk_ev,
                'atk_iv': atk_iv,
                'atk_rank': atk_rank,
                'atk_abi' : atk_abi,
                'atk_item': atk_item,
                'atk_nature': atk_nature,
                'atk_situ': atk_situ,
                'atk_level': atk_level,

                #防御側の情報
                'poke_def': poke_def,
                'def_tera_type': def_tera_type,
                'def_level': def_level,
                'def_ev': def_ev,
                'def_iv': def_iv,
                'def_hp': def_hp,
                'def_iv_hp': def_iv_hp,
                'def_rank': def_rank,
                'def_abi': def_abi,
                'def_item': def_item,
                'def_nature': def_nature,
                'def_situ':def_situ,
                
                #その他の情報
                'poke_env': poke_env,
                'poke_fild': poke_fild,
                'poke_etc': poke_etc,
                'add_dmg': add_dmg,

                #ダメージ
                'max_final_dmg': max_final_dmg,
                'min_final_dmg': min_final_dmg,
                'percent_min_final_dmg' : percent_min_final_dmg,
                'percent_max_final_dmg' : percent_max_final_dmg,
                'percent_for_width': percent_for_width
                }
            
            return render(request, 'result.html', context)
        
        except PokeModel.DoesNotExist:
            error_message = 'ポケモン名に間違いがあります'
            return render(request, 'error.html', {'error_message': error_message})  # エラーメッセージを表示するテンプレートに渡す

        except PokeMove.DoesNotExist:
            error_message = '技名に間違いがあります'
            return render(request, 'error.html', {'error_message': error_message})    

    return render(request, 'pokedmg.html')








