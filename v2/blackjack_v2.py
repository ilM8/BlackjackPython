import random
import os
from tcolor import colors

print(f"{colors.bcolors.ENDC}")

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
    print(f"You currently got{colors.bcolors.yellow}", g.money,f"${colors.bcolors.ENDC}!")
    try:
        g.bet = int(input(f"How much do you want to bet:{colors.bcolors.yellow}"))
        print(f"{colors.bcolors.ENDC}")

    except:
        raise print('Please type in an integer!')
        cls()
        start_game()

    if g.bet > g.money:
        if g.money <= 0:
            print("You don't have any money!")
            play = False
        else:
            print("You can't bet more money than you have!")
            start_game()
    g.money = g.money - g.bet

    cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A",
            "2","3","4","5","6","7","8","9","10","J","Q","K","A",
            "2","3","4","5","6","7","8","9","10","J","Q","K","A",
            "2","3","4","5","6","7","8","9","10","J","Q","K","A",
            "2","3","4","5","6","7","8","9","10","J","Q","K","A",
            "2","3","4","5","6","7","8","9","10","J","Q","K","A",
            "2","3","4","5","6","7","8","9","10","J","Q","K","A",
            "2","3","4","5","6","7","8","9","10","J","Q","K","A",
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
            print("Pot:",g.bet,"$")
            print("")

        if standing == True:

            print("Dealer Cards: [{}] ({})".format("][".join(dealer), dealer_score))
            print("Your Cards: [{}] ({})".format("][".join(player), player_score))
            print("")

            if dealer_score > 21:
                print("Dealer busted!")
                print("")
                g.money = g.money + g.bet*2
                print(f"{colors.bcolors.green}You win{colors.bcolors.yellow}",g.bet,f"${colors.bcolors.ENDC}")

            elif player_score == dealer_score:
                print("Push, nobody wins!")

            elif player_score > dealer_score:
                print("You beat the dealer!")
                print("")
                g.money = g.money + g.bet*2
                print(f"{colors.bcolors.green}You win{colors.bcolors.yellow}",g.bet,f"${colors.bcolors.ENDC}")

            else:
                print("The dealer has a higher score than you!")
                print("")
                print(f"{colors.bcolors.red}You lost{colors.bcolors.yellow}",g.bet,f"${colors.bcolors.ENDC}")
                if g.money <= 0:
                    print("You don't have any money!")
                    exit()

            break

        if first_hand and player_score == 21:
            print("Blackjack!")
            print("")
            g.money = g.money + g.bet*3
            print(f"{colors.bcolors.green}You win{colors.bcolors.yellow}",g.bet*3,f"${colors.bcolors.ENDC}")

            break

        if player_score > 21:
            print("You are too high!")
            print("")
            print(f"{colors.bcolors.red}You lost{colors.bcolors.yellow}",g.bet,f"${colors.bcolors.ENDC}")
            if g.money <= 0:
                print("You don't have any money!")
                break
            break



        print("What would you like to do?")
        print("  [1] Hit  ")
        print("  [2] Stand  ")
        print("  [3] Raise  ")
        print("")
        choice = input("Your Choice: ")
        print("")

        if choice == "1":
            player.append(cards.pop())

        elif choice == "2":
            while calc_hand(dealer) <= 16:
                dealer.append(cards.pop())

            standing = True
        elif choice == "3":
            print(f"You currently got{colors.bcolors.yellow}", g.money,f"${colors.bcolors.ENDC}")
            print("Currently there are", g.bet,"$ in the Pot.")
            print("How much do you want to raise?")
            new_bet = int(input())
            if new_bet > g.money:
                while new_bet > g.money:
                    cls()
                    print("You can't bet more money than you have!")
                    print(f"You currently got{colors.bcolors.yellow}", g.money,f"${colors.bcolors.ENDC}")
                    print("How much do you want to raise?")
                    new_bet = int(input())

            g.bet = g.bet + new_bet
            g.money = g.money - new_bet



        else:
            print("Error: Invalid input. Restart Program")
            start_game()

        first_hand == False

    if play == False:
        exit()

    print("")
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

start_game()
