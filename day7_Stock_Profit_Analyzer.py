prices = [8, 1, 5, 7, 2, 4]

min_price = prices[0]
max_profit = 0
buy_day = 0
sell_day = 0
min_day = 0

for i in range(1, len(prices)):
    profit = prices[i] - min_price

    if profit >max_profit:
        max_profit = profit
        buy_day = min_day
        sell_day = i

    if prices[i] < min_price:
        min_price = prices[i]
        min_day = i

print("Maximum Profit:", max_profit)
print("Buy on day:", buy_day + 1)
print("Sell on day:", sell_day + 1)
