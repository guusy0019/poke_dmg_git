#ポケモンのアイテムの名前から倍率を求めるモジュール
from ..models import PokeModel



#ここでは汎用性を重視するため、最終ダメージを計算したのちに、ダメージの倍率を計算するものとする
#CHOICE_move_class = (('physical', '物理技'), ('special', '特殊技'),('status', '変化技'))

def atk_itemfunc(atk_item, 
                 move_class,
                 poke_effectiveness, 
                 poke_atk, 
                 atk_move_types,
                 poke_env,
                 ):
    item_num = 1

    if atk_item == 'もちものを指定する':
        return item_num
    
    elif atk_item == 'いのちのたま':
        if move_class != 'status':
            item_num = 1.3
            return item_num
        else:
            return item_num
        
    elif atk_item == 'こだわりハチマキ':
        if move_class == 'physical':
            item_num = 1.5
            return item_num   
        else:
            return item_num
    
    elif atk_item == 'こだわりメガネ':
        if move_class == 'special':
            item_num = 1.5
            return item_num
        else:
            return item_num
    
    #効果抜群時DMG1.2倍
    elif atk_item == 'たつじんのおび':
        if poke_effectiveness >=2:
            item_num = 1.2
            return item_num
        else:
            return item_num
    
    elif atk_item == 'ちからのはちまき':
        if move_class == 'physical':
            item_num = 1.1
            return item_num
        else:
            return item_num
        
    
    elif atk_item == 'ものしりメガネ':
        if move_class == 'special':
            item_num = 1.1
            return item_num
        else:
            return item_num
    
    #タイプ強化系とひとくくりにしているため、条件式を当てはめるのは不可能
    #じしゃく、くろおび、どくバリなどをHTMLに追加するのはナンセンスなので避ける
    elif atk_item == 'タイプ強化系':
        item_num = 1.2
        return item_num
    
    #効果としては、一度だけ、そのタイプの技が1.3倍になるというものだが、
    #力不足で一度だけをどういうふうに表現すればいいかわからないのでパス
    elif atk_item == 'ジェル系':
        item_num = 1.3
        return item_num
    
    #カラカラもしくはガラガラ、ガラガラ（アローラ）に持たせるとAが２倍
    #ここでは、ガラガラ（アローラ）をモデルでどのように定義するか未定なので、これは抜かす
    elif atk_item == 'ふといほね':
        if poke_atk == 'カラカラ' or poke_atk =='ガラガラ':
            if move_class == 'physical':
                item_num = 2
                return item_num
            else:
                return item_num
        else: 
            return item_num       
    
    #ピカ様に持たせると、AもCも２倍
    elif atk_item == 'でんきだま':
        if poke_atk == 'ピカチュウ':
            if move_class != 'status':
                item_num = 2
                return item_num
            else:
                return item_num
        else:
            return item_num
    
    elif atk_item == 'しんかいのキバ':
        if poke_atk == 'パールル':
            if move_class == 'special':
                item_num = 2
                return item_num
            else:
                return item_num
        else:
            return item_num
        

    elif atk_item == 'はっきんだま':
        if poke_atk == 'ギラティナ':
            if atk_move_types == 'ドラゴン' or atk_move_types == 'ゴースト':
                item_num = 1.2
                return item_num
            else:
                return item_num
        else:
            return item_num
    
    elif atk_item == 'こころのしずく':
        if poke_atk == 'ラティオス' or poke_atk == 'ラティアス':
            if atk_move_types == 'ドラゴン' or atk_move_types == 'エスパー':
                item_num = 1.2
                return item_num
            else:
                return item_num
        else: 
            return item_num
    
    #天候の影響を受けない
    #例　炎攻撃の場合晴れなら、1.5倍雨なら0.5倍
    #別の関数で天候を考慮するものをつくっているので、それとバッティングしないように
    #たとえば、雨でほのおの場合、別関数で0.5を返しているので、それを１にするために２を返す

    elif atk_item == 'ばんのうがさ':
        if poke_env == 'はれ' and atk_move_types == 'みず':
            item_num = 2
            return item_num
        
        elif poke_env == 'あめ' and atk_move_types == 'ほのお':
            item_num = 2
            return item_num
        
    else:
        return item_num

    
#オボンの実と半減の実はviewの方で処理を分岐して表記する
#ここの関数では最後に✖️で計算するようにしているため、ここに記述すると、ごちゃごちゃしてわかりずらくなるため
def def_itemfunc(def_item,
                 poke_move_class,
                 poke_effectiveness,
                 poke_def,
                 poke_env,
                 poke_before_evolution,
                 atk_move_types,
                 ):
    
    item_num2 = 1

    if def_item == 'もちものを指定する':
        return item_num2
    
    #poke_before_evolution自体がTrueになっている
    elif def_item == 'しんかのきせき':
        if poke_before_evolution:
            item_num2 = 2/3
            return item_num2
        else:
            return item_num2
        
    #とつげきチョッキ
    #Dが1.5倍
    elif def_item == 'とつげきチョッキ':
        if poke_move_class == 'special':
            item_num2 = 2/3
            return item_num2
        else:
            return item_num2


    #毎ターン全体力の1/16回復する
    #つまり、体力に1/16を足す
    elif def_item == 'たべのこし':
        item_num2 = 17/16
        return item_num2

    #効果抜群となる技が半減になる
    elif def_item == '半減実':
        if poke_effectiveness >= 2:
            item_num2 = 1/2
            return item_num2
        else:
            return item_num2
        
    #メタモンに持たせるとBが２倍
    elif def_item == 'メタルパウダー':
        if poke_def == 'メタモン' and poke_move_class == 'physical':
            item_num2 = 1/2
            return item_num2
        else:
            return item_num2
        
    elif def_item == 'しんかいのウロコ':
        if poke_def == 'パールル' and poke_move_class == 'special':
            item_num2 = 1/2
            return item_num2
        else:
            return item_num2
        
        #はれでほのおの場合1.5倍つまり3/2倍なので2/3を返す
    elif def_item == 'ばんのうがさ':
        if poke_env == 'はれ' and atk_move_types == 'ほのお':
            item_num2 = 2/3
            return item_num2
        
        elif poke_env == 'あめ' and atk_move_types == 'みず':
            item_num2 = 2/3
            return item_num2
        
        else:
            return item_num2
    
    else:
        return item_num2
