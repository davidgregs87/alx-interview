#!/usr/bin/python3
'''
Task Solution
'''


def makeChange(coins, total):
    '''
    determines the fewest number of coins needed to meet a given total
    '''
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    no_of_coins = 0
    for coin in coins:
        while total > 0:
            if total // coin > 0:
                no_of_coins += 1
                total -= coin
            else:
                break
    return -1 if total > 0 else no_of_coins
