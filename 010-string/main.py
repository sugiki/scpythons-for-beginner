# 行頭に # を書くと、プログラムとして処理されない文字列（コメントと呼ばれます）を書くことができます

# 文字列は + の記号を使うことにより連結ができます

string001 = 'Che'
string002 = 'Guevara'
string003 = string001 + string002

assert(string003 == 'CheGuevara')

# TODO string001とstring002ともう1つ、自分で文字列をstring003用意して以下を成立させてください
# TODO string004 = ...

assert(string004 == 'Che Guevara')

# * を使うと文字を繰り返して連結することができます

string005 = 'yah' * 3
assert(string005 == 'yahyahyah')

# 型(テンプレート)となる文字列を用意しておいて、対象によって内容を入れ替える

string006 = '{0} {1}さん、こんにちは'
string007 = string006.format('Che', 'Guevara')
assert(string007 == 'Che Guevaraさん、こんにちは')

# TODO 同様の方法で、string006を使用してRyoma Sakamotoさんに挨拶をしてください
# TODO string008 = ...

assert(string008 == 'Ryoma Sakamotoさん、こんにちは')

# 文字列の置換

string009 = 'Everyday is holiday.'
string010 = string009.replace('holiday', 'workday until you gonna die')
assert(string010 == 'Everyday is workday until you gonna die.')

# TODO 同様の方法で、string009を使用してSunday is holiday. という文章を作ってください
# TODO string011 = ...

assert(string011 == 'Sunday is holiday.')


string012 = '9e7bd0d10e0e29d7e597bidi9ed591j62f8fa1462ggjii5fd57hj6c1j957i2c8a7hg5b0gc5cif9j643fig258733je25fjjbd0f6f98he30def5391a49d82e61d14adcc022fa69jbg01i914dehg63j7069b14226c73ca63bggfa7cag83ae5igj5060jh6gj2eg0g7j82c54cifg3j0d7670g705cfa705hag7i19i5319e49hfd43d4i4966d30fd9444ej5e543i0hi9a71ee7d0272iefj8h367e0jhb0bi8bag5b8505jb359h96d38i2d02ch7939a2i6125b895h6965cg33hja6993859h822d2982ge835gij36dgacef81h6hcg3cja22711751fcfjgg330f4hh013d05aa5ej274e0gd38gac37792c096803dgbje7f89a5h68f2eejj6d4i2hefbdf2cf2acicehjf6dgb8bh4fc63eh429ba74h2ca01131f7913h2edd1heh6c69jba2f7bf950bij0h69defieff20cfdch83fg28hhibdbdd18ji34589h108a9j7bb38gdc825iaj59dij8hfa7j2ga16387a9a24bjibj128j7b942e57gh5b1ef1die05c5bh464a88ad42ahdja0jaiejegadh16ca0h86b3h9h06333a0j7h50g1h83h177bhiej2d5g7a065c152chh62ge51a9b34h61g4a498305ccc5fc4a52h4562de8393f1bgga45bj9415ce327dc2b72gc3ege6je5h537a826gf6h91a53cj07377a86i39bcejh2b7ca6f9b73209hcg7c35ajf4hgc2fgjf70j0bf3ba55c365fj83agbdjifi62i7bej311b767d2bj1i34c0gd0g8g3je51j735a4ci8eb7643729820g'

# 文字列の検索、文字列に単語が含まれるかを探すことができます
# 見つかった場合はその文字のある場所を(一番左の文字が0番目)、見つからない場合は-1が帰ってきます
assert(string009.find('day') == 5)
# 文字列にdieが含まれていないことを意味する
assert(string009.find('die') == -1)

# TODO string012にkが含まれていないことを確かめてください
assert(string012.find('k') == ...)

# 文字列の出現頻度、文字列に単語が何回出てくるかを探すことができます
assert(string009.count('day') == 2)
# 文字列にdieが含まれていないことを意味する
assert(string009.count('die') == 0)

# TODO string012にiが38回出てくることを確かめてください
assert(... = 38)

print('全問正解です！おめでとうございます！')
print('あなたは与えられたすべての問題を解きました！')
