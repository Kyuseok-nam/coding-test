money = int(input())
stock_prices = list(map(int,input().split()))

jun_money,sung_money = money, money
jun_stock, sung_stock = 0,0

for i in range(len(stock_prices)):
    price = stock_prices[i]
    if jun_money >= price:
        jun_buy = jun_money//price
        jun_stock += jun_buy
        jun_money -= price*jun_buy
    if i>=3:
        if stock_prices[i]<stock_prices[i-1]<stock_prices[i-2]<stock_prices[i-3] and sung_money >= price:
            sung_buy = sung_money//price
            sung_stock+=sung_buy
            sung_money -= sung_buy*price
        elif stock_prices[i] > stock_prices[i-1] > stock_prices[i-2] > stock_prices[i-3] and jun_stock !=0:
            sung_money += sung_stock*price
            sung_stock = 0

if jun_money+(stock_prices[-1]*jun_stock)>sung_money+(stock_prices[-1]*sung_stock):
    print("BNP")
elif jun_money+(stock_prices[-1]*jun_stock)<sung_money+(stock_prices[-1]*sung_stock):
    print("TIMING")
else:
    print("SAMESAME")    
