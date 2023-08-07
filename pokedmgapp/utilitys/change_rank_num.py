
#ランクを最後に✖️ために１〜６までの数値を変換

#攻撃ランクを変換
def change_atk_rank_num(def_rank):
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
