import random
import os

class g:
    bet = 0
    money = 0


def cls():
    os.system("cls" if os.name == "nt" else "clear")

def calc_hand(hand):
    sum = 0

    non_aces = [card for card in hand if card != "A"]
    aces = [card for card in hand if card == "A"]

    for card in non_aces:
        if card in "JQK":
            sum += 10

        else:
            sum += int(card)

    for card in aces:
        if sum <= 10:
            sum +=  11

        else:
            sum += 1

    return sum

g.money = 2000

def start_game():
    play = True
    print("You currently got " , g.money , "!")
    g.bet = int(input("How much do you want to bet: "))
    if g.bet > g.money:
        if g.money <= 0:
            print("You don't have any money!")
            play = False
        else:
            print("You can't bet more money than you have!")
            start_game()

    cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A",
            "2","3","4","5","6","7","8","9","10","J","Q","K","A",
            "2","3","4","5","6","7","8","9","10","J","Q","K","A",
            "2","3","4","5","6","7","8","9","10","J","Q","K","A"
    ]
    random.shuffle(cards)

    dealer = []
    player = []

    for i in range(2):
        dealer.append(cards.pop())
        player.append(cards.pop())

    standing = False

    first_hand = True


    while play == True:
        cls()
        player_score = calc_hand(player)
        dealer_score = calc_hand(dealer)

        if standing == False:

            print("Dealer Cards: [{}] [?]".format(dealer[0]))
            print("Your Cards: [{}] ({})".format("][".join(player), player_score))
            print("")

        if standing == True:

            print("Dealer Cards: [{}] ({})".format("][".join(dealer), dealer_score))
            print("Your Cards: [{}] ({})".format("][".join(player), player_score))

            if dealer_score > 21:
                print("Dealer busted, you win!")
                g.money = g.money + g.bet

            elif player_score == dealer_score:
                print("Push, nobody wins!")

            elif player_score > dealer_score:
                print("You beat the dealer, you win!")
                g.money = g.money + g.bet

            else:
                print("You lose!")
                g.money = g.money - g.bet
                if g.money <= 0:
                    print("You don't have any money!")
                    break

            break

        if first_hand and player_score == 21:
            print("Blackjack!")
            g.money = g.money + g.bet*3

            break

        if player_score > 21:
            print("You lose!")
            g.money = g.money - g.bet
            if g.money <= 0:
                print("You don't have any money!")
                break
            break



        print("What would you like to do?")
        print("  [1] Hit  ")
        print("  [2] Stand  ")
        print("")
        choice = input("Your Choice: ")
        print("")

        if choice == "1":
            player.append(cards.pop())

        elif choice == "2":
            while calc_hand(dealer) <= 16:
                dealer.append(cards.pop())

            standing = True

    if play == False:
        exit()


    print("Do you want to play again?")
    print("  [1] Play Again  ")
    print("  [2] Exit  ")
    choice = "0"
    while True:
        choice = input()

        if choice == "1":
            start_game()
            break

        elif choice == "2":
            print("Good Bye")
            break

        else:
            print("Error 400")

start_game()
