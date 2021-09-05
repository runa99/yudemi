# 関数１
def add(a, b):  # a,b　引数であり変数
    c = a + b  # すべて変数
    return c  # C返り値であり変数 （文字列　関数ではないものは変数）addの返り値は変数 リターンの右にあるものを返してね


c = add(10, 5)  # addの返り値をdに代入する
print(c)

# 関数２


def sum(values: list) -> int:
    sum_value = 0
    for v in values:
        sum_value = sum_value + v
    return sum_value
