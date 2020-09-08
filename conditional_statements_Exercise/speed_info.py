speed = float (input())

if speed <= 10:
    print('slow')
elif 10 < speed <= 50: #е същото като speed <= 50:
    print('average')
elif speed <= 150:
    print('fast')
elif speed <= 1000:
    print('ultra fast')
else:
    print('extremely fast')