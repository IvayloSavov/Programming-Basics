change = float(input()) * 100

counter = 0
while change > 0:
    if change >= 200:
        counter += change // 200 #като го разделим ще разберем колко пъти стотинките се събират вътре съответно колко монети ще са не обходими
        change %= 200 # остатъкът ще е след като се махнат тези 200 стотинки пример 360 махаме 200 остават 160
    if change >= 100:
        counter += change//100
        change %= 100
    if change >= 50:
        counter += change//50
        change %= 100