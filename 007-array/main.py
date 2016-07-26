# 行頭に # を書くと、プログラムとして処理されない文字列（コメントと呼ばれます）を書くことができます

# 名前がarray1の配列を用意します
array1 = []

# array1 は [] と同じです
assert(array1 == [])

# 中に何も入っていないので size は 0 です
assert(len(array1) == 0)

# array1 に何かを追加してみます
array1.append('何か')

# 何かが入りました
assert(array1 == ['何か'])
# sizeも変わりました
assert(len(array1) == 1)

# 今度は数値を追加してみます
array1.append(30)

# 入りました
assert(array1 == ['何か', 30])
assert(len(array1) == 2)

# TODO ここで、何かを追加してみてください
# 追加された配列が等しいことを確かめてください
# TODO

# 一つ増えたことにより size = 3 になりました
assert(len(array1) == 3)

 # 一番左(先頭) にある値が欲しい時は以下のようにします
assert(array1[0] == '何か')

# 数値が 1 ではなく 0 であることに注意してください
# TODO では、30を取り出してください
assert(''' 実装してください ''' == 30)

# 次に以下のような配列array2を使います
array2 = [1, 2, 3, 3, 3, 2, 1]

# この配列の中に1は2個あります
assert(array2.count(1) == 2)

# TODO では、この中に3は何個ありますか
assert(array2.count(3) == ''' 実装してください ''')

#　この配列で、最初に2が出てくる場所は何番目ですか？
assert(array2.index(2) == 1)
# 答えは1番目です。なぜなら、その左隣の1は0番目だからです
assert(array2.index(1) == 0)

# TODO では、3は何番目ですか？
assert(array2.index(3) == ''' 実装してください ''')
