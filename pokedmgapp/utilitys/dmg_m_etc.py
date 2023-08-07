from ..models import PokeModel, PokeMove

#   ダメージ = (((レベル×2/5+2)×威力×A/D)/50+2)×範囲補正×おやこあい補正
#   ×天気補正×急所補正×乱数補正×タイプ一致補正×相性補正×やけど補正×M×Mprotect
#   部分のM部分と急所補正の関数を記述

#  M部分↓
#  M=壁補正×ブレインフォース補正×スナイパー補正×いろめがね補正
#  ×もふもふほのお補正×Mhalf×Mfilter×フレンドガード補正×たつじんのおび補正
#  ×メトロノーム補正×いのちのたま補正×半減の実補正×Mtwice

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
    
        
        







