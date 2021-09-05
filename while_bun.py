count = 0
score = 80

while count < 100:  # カウントが100未満の限りture
    print(count)  # カウント出力
    count += 1  # カウント＋１
    if count == score:  # もしカウントがスコアと等しくなったら
        print(score)  # スコアをプリントしてね
        break  # とめてね
