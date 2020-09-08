# 1. Read input data
number_to_convert = float(input())
metric_to_convert = input()
converted_metric = input()

if metric_to_convert == 'm' and converted_metric == 'cm':
    number_to_convert *= 100
    print(f'{number_to_convert:.3f}')
elif metric_to_convert == 'm' and converted_metric == 'mm':
    number_to_convert *= 1000
    print(f'{number_to_convert:.3f}')
elif metric_to_convert == 'cm' and converted_metric == 'mm':
    number_to_convert *= 10
    print(f'{number_to_convert:.3f}')
elif metric_to_convert == 'cm' and converted_metric == 'm':
    number_to_convert /= 100
    print(f'{number_to_convert:.3f}')
elif metric_to_convert == 'mm' and converted_metric == 'cm':
    number_to_convert /= 10
    print(f'{number_to_convert:.3f}')
elif metric_to_convert == 'mm' and converted_metric == 'm':
    number_to_convert /= 1000
    print(f'{number_to_convert:.3f}')