# 行頭に # を書くと、プログラムとして処理されない文字列（コメントと呼ばれます）を書くことができます

# 以下の例にならって、関数を実装してください
# ex. hello world と返却する関数hello
def hello():
    return 'hello world'

# 1. 引数にかかわらず ignored と返却する関数 ignore
def ignore(x):
    return 'ignored'

# 与えられた数値の引数x を +1 して返却する関数 increment
def increment(x):
    return x + 1

assert(hello() == 'hello world')
assert(ignore(1) == 'ignored')
assert(ignore('1') == 'ignored')
assert(increment(0) == 1)
assert(increment(11) == 12)

print('全問正解です！おめでとうございます！')
print('あなたは与えられたすべての問題を解きました！')
