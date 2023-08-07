#四捨五入関数
#int関数は少数部分を切り捨てる　例　4.89 output → ４
def round_4_5(n):
    if n >= 0:
        n = int(n + 0.5)
        return n
    else:
        n = int(n -0.5)
        return n

#五捨五超入関数
#5を超えたら繰り上げ、５以下は切り捨て
def round_5_5(n):
    #正数部分を取得
    positive_num = int(n)
    #少数部分を取得
    decimal_num = n - positive_num

    if decimal_num > 0.5:
        #5を超えた場合繰り上げる処理
        positive_num += 1
        return positive_num
    
        #0.5を超えない場合切り捨てて、正数部分をそのまま返す
    else:
        return positive_num
    
#繰り上げ関数
#小数点が０よりも大きい場合、小数点以下を切り捨てて、１繰り上げる
def round_up(n):
    positive_num = int(n)
    decimal_num = n - positive_num

    if decimal_num > 0:
        positive_num += 1
        return positive_num

    
#切り捨て関数はint()にぶち込めばいいだけ

    
