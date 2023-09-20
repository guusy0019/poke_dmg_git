from ..models import PokeModel, PokeMove

#   ダメージ = (((レベル×2/5+2)×威力×A/D)/50+2)×範囲補正×おやこあい補正
#   ×天気補正×急所補正×乱数補正×タイプ一致補正×相性補正×やけど補正×M×Mprotect
#   部分のM部分と急所補正の関数を記述

#  M部分↓
#  M=壁補正×ブレインフォース補正×スナイパー補正×いろめがね補正
#  ×もふもふほのお補正×Mhalf×Mfilter×フレンドガード補正×たつじんのおび補正
#  ×メトロノーム補正×いのちのたま補正×半減の実補正×Mtwice

##ここにかいてあるM部分の技の追加効果の補正や、アイテム補正は別のモジュールとして別記
##掛け算だからどこでかけても一緒、つまり技追加効果関数はまとめてあげたほうが、メンテナンスや拡張しやすい

#壁補正関数
def wall_correct(request, poke_wall, poke_move_kinds):
    if poke_wall is None:
        return 1
    
    wall_modifier_value = 1
    if 'reflect' in  poke_wall and poke_move_kinds == 'physical':
        wall_modifier_value = 0.5
        return wall_modifier_value
    elif 'light_screen' in poke_wall and poke_move_kinds == 'special':
        wall_modifier_value = 0.5
        return wall_modifier_value
    else:
        return wall_modifier_value
    
        
    #きのみの回復分の条件式を追加
    #絶対にきのみが発動するpercent_min_final_dmg,max_remaining_hpを使用する
    #オボンは体力が半分以下になると発動する
    #混乱実は体力が1/4以下になると発動
    #それぞれ回復分の値を取り出し変数に格納してprogressの追加バーに記述
    #体力が０になった場合にバーに回復分を表示させないための条件式を追加
def heal_value_func(def_item, 
                    percent_min_final_dmg, 
                    max_remaining_hp,
                    def_poke_hp
                    ):
    if def_item == 'オボンの実' and percent_min_final_dmg >= 50 and max_remaining_hp > 0:
        heal_value_num = def_poke_hp / 4
        return heal_value_num
    
    elif def_item == 'オボンの実' and max_remaining_hp <= 0:
        heal_value_num = 0
        return heal_value_num
            
    elif def_item == '混乱実' and percent_min_final_dmg >= 75 and max_remaining_hp > 0:
        heal_value_num = def_poke_hp / 3
        return heal_value_num

    elif def_item == '混乱実' and max_remaining_hp <= 0:
        heal_value_num = 0
        return heal_value_num

    else:
        heal_value_num = 0
        return heal_value_num


#乱数マックス時のmaxDMG - minDMGのあまり
#普通に記述してしまうとHPが０になった場合でも、バーに表示されてしうため
#そのためHP > 0の時点でreturn 0を返すようにする
def hp_adjustment_func(percent_for_max_width,
                       max_remaining_hp
                       ):
    if max_remaining_hp > 0:
        return percent_for_max_width
    else:
        return 0
    

#フィールド系の補正関数
def field_value_func(poke_field, move_types, poke_move):
    field_value_num = 1
    glass_field_effect_move = ['じしん', 'じならし', 'マグニチュード']

    #電気タイプの技が1.3倍になるだけ
    if poke_field == 'エレキフィールド' and move_types == 'でんき':
        field_value_num = 1.3
        return field_value_num
    
    #くさタイプの技が1.3倍, また、じしん、じならし、マグニチュードのDMGが半減
    #くさタイプの攻撃かつ半減になる攻撃は存在しないので考慮しなくてよい、いちおうelseしとくが
    elif poke_field == 'グラスフィールド':
        if poke_move in glass_field_effect_move:
            field_value_num = 0.5
            return field_value_num
        
        elif move_types == 'くさ':
            field_value_num = 1.3
            return field_value_num
        
        else:
            return field_value_num
    
    #ミストシードをもっているとDが一段階上がるが、これはユーザーがあげる
    #ドラゴンタイプのDMGが半減
    elif poke_field == 'ミストフィールド' and move_types == 'ドラゴン':
        field_value_num = 0.5
        return field_value_num
    
    #サイコシードを持っていると、Dが一段階上がるが無視
    #エスパータイプの技が1.3倍
    elif poke_field == 'サイコフィールド' and move_types == 'エスパー':
        field_value_num = 1.3
        return field_value_num
    
    else:
        return field_value_num

            
            

    







