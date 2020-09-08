# 1. Read input data
budget = float(input())
number_video_cards = int(input())
number_processors = int(input())
number_ram_memory = int(input())
# 2. Prices
price_video_card = number_video_cards * 250
price_processors = price_video_card * 35/100 * number_processors
price_ram_memory = price_video_card * 10/100 * number_ram_memory
# 3. Total
total = price_video_card + price_processors + price_ram_memory
if number_video_cards > number_processors:
    total *= 0.85
left_need_budget = abs(total-budget)
if budget >= total:
    print(f"You have {left_need_budget:.2f} leva left!")
else:
    print(f"Not enough money! You need {left_need_budget:.2f} leva more!")