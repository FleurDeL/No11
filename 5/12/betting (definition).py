def guessed_card(number, suit, bet):
    money_won = 0
    guessed = False
    if number == 8 and suit == 'hearts':
        money_won = 10*bet
        guessed = True
    else:
        money_won = bet/10


    return (10*bet,guessed)

print(guessed_card(8, 'hearts', 10))