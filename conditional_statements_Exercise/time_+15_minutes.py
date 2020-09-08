# 1. Read input data
hours = int(input())
minutes = int(input())
# 2. +15 minutes
minutes += 15

if minutes > 59:
    hours += 1
    #minutes -= 60 #вместо модулно деление
if hours > 23:
    hours = 0
    # hours -= 24 вместо hours = 0

minutes = minutes % 60 #модулното деление се извършва и има ефект само когато числото, което се дели е по-голямо от числото, на което делим
# и това модулно показва с колко минути се надвишава
if minutes < 10:
    print(f'{hours}:0{minutes}')
else:
    print(f'{hours}:{minutes}')