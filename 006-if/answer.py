# 行頭に # を書くと、プログラムとして処理されない文字列（コメントと呼ばれます）を書くことができます

# 以下の例にならって、関数を実装してください
# ex. 与えられた引数aが偶数のときは 'EVEN' 奇数の時は 'ODD' と返却する関数 even_odd
def even_odd(a):
    if a % 2 == 0:
        return 'EVEN'
    return 'ODD'

# の次の行は、4個の空白が必要です（これをインデントよびます）
# インデントは、キーボード左上にある、横長のキー Tab キーで入力できます
# functionでも同じものがありました

# 1. 与えられた引数aをa月として、その月の最大の日数を返却する関数dates_of_month
def dates_of_month(a):
    if a == 1:
        return 31
    if a == 2:
        return 29
    if a == 3:
        return 31
    if a == 4:
        return 30
    if a == 5:
        return 31
    if a == 6:
        return 30
    if a == 7:
        return 31
    if a == 8:
        return 31
    if a == 9:
        return 30
    if a == 10:
        return 31
    if a == 11:
        return 30
    if a == 12:
        return 31

# 与えられた文字列stringの文字数が、x文字より多いなら 'x文字より多いです'
# ちょうどx文字なら 'x文字です'
# x文字以下なら 'x文字より少ないです' と返却する関数 char_length
def char_length(string, x):
    length = len(string)
    str_x = str(x)
    if x < length:
        return str_x + '文字より多いです'
    if x > length:
        return str_x + '文字より少ないです'
    return str_x + '文字です'
    # ここを実装します
    pass


assert(even_odd(0) == 'EVEN')
assert(even_odd(1) == 'ODD')
assert(even_odd(2) == 'EVEN')
assert(even_odd(99) == 'ODD')
assert(even_odd(-98) == 'EVEN')

assert(dates_of_month(1) == 31)
assert(dates_of_month(2) == 29)
assert(dates_of_month(3) == 31)
assert(dates_of_month(4) == 30)
assert(dates_of_month(5) == 31)
assert(dates_of_month(6) == 30)
assert(dates_of_month(7) == 31)
assert(dates_of_month(8) == 31)
assert(dates_of_month(9) == 30)
assert(dates_of_month(10) == 31)
assert(dates_of_month(11) == 30)
assert(dates_of_month(12) == 31)

assert(char_length('練習用', 2) == '2文字より多いです')
assert(char_length('練習用', 3) == '3文字です')
assert(char_length('練習用', 4) == '4文字より少ないです')
assert(char_length('マンゴー', 3) == '3文字より多いです')
assert(char_length('マンゴー', 4) == '4文字です')
assert(char_length('マンゴー', 5) == '5文字より少ないです')

print('全問正解です！おめでとうございます！')
print('あなたは与えられたすべての問題を解きました！')
