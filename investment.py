#!/usr/bin/env python3
amount = float(input('Enter amount:'))#输入金额
inrate = float(input('Enter Interest rate:'))#输入利率
period = int(input('Enter period:'))#输入期限
value = 0
year = 1
while year <= period:
    amount = amount + (inrate*amount)
    print('Year {} Rs. {:.2f}'.format(year, amount))
    #amount = value
    year = year + 1
