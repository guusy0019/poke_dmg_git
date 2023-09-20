
#ランクを最後に✖️ために１〜６までの数値を変換

#攻撃ランクを変換
def change_atk_rank_num(atk_rank):
    atk_rank_num = 1
    if atk_rank == '0':
        return atk_rank_num

    elif atk_rank == '1':
        atk_rank_num = 1.5
        return atk_rank_num

    elif atk_rank == '2':
        atk_rank_num = 2
        return atk_rank_num

    elif atk_rank == '3':
        atk_rank_num = 2.5
        return atk_rank_num

    elif atk_rank == '4':
        atk_rank_num = 3
        return atk_rank_num

    elif atk_rank == '5':
        atk_rank_num = 3.5
        return atk_rank_num

    elif atk_rank == '6':
        atk_rank_num = 4
        return atk_rank_num
    
    elif atk_rank == '-1':
        atk_rank_num = 2/ 3
        return atk_rank_num

    elif atk_rank == '-2':
        atk_rank_num = 2/4
        return atk_rank_num

    elif atk_rank == '-3':
        atk_rank_num = 2/5
        return atk_rank_num

    elif atk_rank == '-4':
        atk_rank_num = 2/6
        return atk_rank_num

    elif atk_rank == '-5':
        atk_rank_num_rank_num = 2/7
        return atk_rank_num

    elif atk_rank == '-6':
        atk_rank_num = 2/8
        return atk_rank_num
    
#防御ランクを変換
def change_def_rank_num(def_rank):
    def_rank_num = 1
    if def_rank == '0':
        return def_rank_num

    elif def_rank == '1':
        def_rank_num = 1.5
        return def_rank_num

    elif def_rank == '2':
        def_rank_num = 2
        return def_rank_num

    elif def_rank == '3':
        def_rank_num = 2.5
        return def_rank_num

    elif def_rank == '4':
        def_rank_num = 3
        return def_rank_num

    elif def_rank == '5':
        def_rank_num = 3.5
        return def_rank_num

    elif def_rank == '6':
        def_rank_num = 4
        return def_rank_num
    
    elif def_rank == '-1':
        def_rank_num = 2/ 3
        return def_rank_num

    elif def_rank == '-2':
        def_rank_num = 2/4
        return def_rank_num

    elif def_rank == '-3':
        def_rank_num = 2/5
        return def_rank_num

    elif def_rank == '-4':
        def_rank_num = 2/6
        return def_rank_num

    elif def_rank == '-5':
        def_rank_num = 2/7
        return def_rank_num

    elif def_rank == '-6':
        def_rank_num = 2/8
        return def_rank_num
