import random
lang = ['p', 'y', 't', 'h', 'o', 'n']

random.shuffle(lang)  # langという変数を　ランダムにシャッフルしてね
new_lang = ''.join(lang)  # langという変数を’’を抜いて結合して、new_langに代入してね
print(new_lang)
