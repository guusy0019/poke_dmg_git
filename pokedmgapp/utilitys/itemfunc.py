#ポケモンのアイテムの名前から倍率を求めるモジュール
from ..models import PokeModel

def atk_itemfunc(request):
    item = request.POST.get('atk_item')
    
    if item == 'inotinotama':
        item_mag = 1.3
    
    elif item == 'hatimaki':
        item_mag = 1.5
    
    elif item == 'megane':
        item_mag = 1.5
    
    elif item == 'tatuzinnoobi':
        item_mag = 1.2
    
    elif item == 'tikaranohaitmaki':
        item_mag = 1.1
    
    elif item == 'monosirimegane':
        item_mag = 1.1
    
    elif item == 'taipukyouka':
        item = 1.2
    
    elif item == 'zyeru':
        item_mag = 1.3
    
    elif item == 'hutoihone':
        item_mag = 2.0
    
    elif item == 'dennkidama':
        item_mag = 2.0
    
    elif item == 'sinnkainokiba':
        item_mag = 2.0
    
    elif item == 'hakkinndama':
        item_mag = 1.2
    
    elif item == 'kokoronosizuku':
        item_mag = 1.2
    
    #ばんのうがさの場合のみ天候の影響を受けないので、値をとりあえず１．０にした
    elif item == 'bannnougasa':
        item_mag = 1.0
    
    else:
        item_mag = 1
    

def def_itemfunc(request):
    item2 = request.POST.get('def_item')
    if item2 == 'sinnkanokiseki':
        item_mag2 = 1.5
    
    elif item2 == 'totugekityokki':
        item_mag2 = 1.5
    
    #体力が1/2以下になったときに全体力の1/4回復する
    elif item2 == 'obonnnomi':
        pass

    #毎ターン全体力の1/16回復する
    elif item2 == 'tabenokosi':
        pass

    #体力が1/4以下になった時に全体力の1/3回復する
    elif item2 == 'konnrannmi':
        pass

    #効果抜群となる技が半減になる
    elif item2 == 'hanngennmi':
        pass

    elif item2 == 'metarupauda':
        item_mag2 = 2

    elif item2 == 'bannnougasa':
        item_mag2 = 1

    else:
        item_mag = 1

