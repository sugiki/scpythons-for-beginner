# 行頭に # を書くと、プログラムとして処理されない文字列（コメントと呼ばれます）を書くことができます

# ファイルを開くには open を使います
# ファイルを読み込めないときは、プログラムを実行するディレクトリを変更する必要があります
# 読み込めない時は声をかけてください

file = open('011.csv', 'r')

for line in file:
    # これでlineには、読み込んだファイルの1行ずつが入っています
    # print(line) でその1行を表示させられます
    # print(line)
    pass


# ファイルを開いた時は、最後に必ずこの文章を入れましょう(ファイルを閉じます)
file.close()

# TODO このファイルを読み込み、最も大きな数値maxともっと小さな数値minを計算してください
# 読み込んだ時の一業は文字列(string)として読み込まれます
# 読み込んだ文字列(string)をまず、分解(split)し、数値に変換します

file = open('011.csv', 'r')

min = 100000
max = -100000

for line in file:
    numbers = line.split(',')
    # TODO

assert(min == -9998)
assert(max == 9991)

file.close()
