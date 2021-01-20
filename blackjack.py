import random

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4 * 6


class PlayerProfile:
    def __init__(self, name):
        dummy = 0
        temp = []
        self.name = name
        self.hand = temp
        self.score = total(self.hand)
        self.cash = 0
        self.bet_size = 100
        self.win = dummy
        self.lose = dummy
        self.round_result = dummy
        self.winnings = dummy
        self.blackjack = dummy
        self.blackjack_counter = dummy
        self.games = dummy


    def show_detail(self):
        self.score = total(self.hand)
        print(self.name + ": " + str(self.hand))
        print("Score:", self.score)
        print("Cash:", self.cash, "\n")

    def show_cash(self):
        print(self.name)
        print("Cash:", self.cash, "\n")

    def player_summary(self):
        win_rate = float(self.win * 100 / self.games)
        lose_rate = float(self.lose * 100 / self.games)
        draw_rate = 100 - win_rate - lose_rate
        draw_rate = format(draw_rate, '.2f')
        blackjack_rate = float(self.blackjack_counter*100 / self.games)
        print(self.name)
        print("Wins:", self.win)
        print("Loses:", self.lose)
        print("Draws:", iteration - self.win - self.lose)
        print("Games played:", self.games)
        print("Winnings:", self.cash)
        print("Win rate:", str(win_rate) + "%")
        print("Lose rate:", str(lose_rate) + "%")
        print("Draw rate:", str(draw_rate) + "%")
        print("BlackJacks:", self.blackjack_counter)
        print("BlackJack rate:", str(blackjack_rate) + "%")
        print("\n")

    def dealer_summary(self, player_num):
        dealer_draw = self.games - self.win - self.lose
        dealer_win_rate = float(self.win * 100 / self.games)
        dealer_lose_rate = float(self.lose * 100 / self.games)
        dealer_draw_rate = 100 - dealer_win_rate - dealer_lose_rate
        dealer_draw_rate = format(dealer_draw_rate, '.2f')
        blackjack_rate = float(self.blackjack_counter*100 / (self.games/player_num))
        print("Dealer")
        print("Wins:", self.win)
        print("Loses:", self.lose)
        print("Draws:", dealer_draw)
        print("Games played:", self.games)
        print("Winnings:", self.cash)
        print("Win rate:", str(dealer_win_rate) + "%")
        print("Lose rate:", str(dealer_lose_rate) + "%")
        print("Draw rate:", str(dealer_draw_rate) + "%")
        print("BlackJacks:", self.blackjack_counter)
        print("BlackJack rate:", str(blackjack_rate) + "%")

def display_cash(dealer_data, player_data):
    for i in player_data:
        i.show_cash()

    dealer_data.show_cash()

def total(hand):
    total = 0

    for card in hand:
        if card == "J" or card == "K" or card == "Q":
            total += 10
        elif card == "A":
            if total >= 11:
                total += 1
            else:
                total += 11
        else:
            total += card

    return total

def participants(player_num):
    temp = []
    for i in range(player_num):
        i += 1
        player = "Player " + str(i)
        temp.append(player)

    return temp

def display_player_info(player_data):
    for i in player_data:
        i.show_detail()


def display_dealer_info(dealer_data):
    dealer_data.show_detail()

def set_player_profile(player_list):
    temp = []
    for i in player_list:
        data = PlayerProfile(i)
        data.cash = 0
        temp.append(data)
    return temp

def set_dealer_profile():
    data = PlayerProfile("Dealer")
    data.cash = 0
    return data

def hit(deck):
    card = deck.pop()
    if card == 11: card = "J"
    if card == 12: card = "Q"
    if card == 13: card = "K"
    if card == 14: card = "A"
    return card

def deal(dealer_data, player_data, deck):
    # distribute card in clockwise (player 1, 2, 3 .. dealer then repeat once more for second card)
    temp_list = []
    for i in player_data:
        temp_list.append(i)

    temp_list.append(dealer_data)
    pnum = len(temp_list)


    card1 = []
    card2 = []
    for i in range(pnum*2):
        card = hit(deck)
        if i >= pnum:
            card2.append(card)
        else:
            card1.append(card)

    i = 0
    for j in temp_list:
        temp = []
        temp.append(card1[i])
        temp.append(card2[i])
        j.hand = temp
        print(j.name, "has", temp)
        i += 1
    print("\n")

def print_results(dealer, player):
    print("The dealer has a " + str(dealer.hand) + " for a total of " + str(dealer.score))
    print(player.name, "have a " + str(player.hand) + " for a total of " + str(player.score))



def blackjack(dealer_data, player_data):
    if dealer_data.score == 21:
        print("Dealer got a Black Jack")
        dealer_data.blackjack_counter += 1

        for i in player_data:
            if i.score == 21:
                print(i.name, "also has BlackJack. It's a standoff\n")
                i.games += 1
                dealer_data.games += 1
                i.blackjack_counter += 1
            else:
                print(i.name, "Loses to Dealer's Blackjack")
                lose(dealer_data, i)
        return 1

    else:
        for i in player_data:
            if i.score == 21:
                print(i.name, "has BlackJack.", i.name, "win!")
                i.blackjack_counter += 1
                i.blackjack = 1
                win(dealer_data, i, 1.5)
            else:
                continue

def player_draw(dealer_data, player_data, deck):

    for i in player_data:
        if i.score == 21:
            pass
        else:
            print(i.name + "'s turn")
            print("Current deck:", i.hand)
            print("Current score is", i.score, "\n")
            if i.score >= 17:
                print(i.name, "will stay\n")
            else:
                print(i.name, "will hit\n")
                while i.score < 17:
                    new_card = hit(deck)
                    print(i.name, "got a", new_card, "\n")
                    i.hand.append(new_card)
                    i.score = total(i.hand)
                    print(i.name + "'s new hand is", i.hand)
                    print("Score:", i.score, "\n")

                if i.score > 21:
                    print(i.name, "busted")
                    lose(dealer_data, i)

                else:
                    print(i.name, "will stay\n")

            print("End of turn\n")
    print("End of Players' card draw\n")

def dealer_draw(dealer_data, deck):
    print("Dealer's turn\n")
    print("Current deck:", dealer_data.hand)
    print("Current score is", dealer_data.score, "\n")
    if dealer_data.score >= 17:
        print("Dealer will stay")
    else:
        print("Dealer will hit")
        while dealer_data.score < 17:
            new_card = hit(deck)
            print("Dealer got a", new_card, "\n")
            dealer_data.hand.append(new_card)
            dealer_data.score = total(dealer_data.hand)
            print("Dealer's new hand is", dealer_data.hand)
            print("Score:", dealer_data.score, "\n")
    print("End of dealer turn\n")

def score(dealer_data, player_data):
    print("Checking score\n")
    for i in player_data:
        if i.score > 21 or i.blackjack == 1:
            pass
        else:
            print_results(dealer_data, i)
            if dealer_data.score <= 21:
                if i.score == dealer_data.score:
                    i.games += 1
                    dealer_data.games += 1
                    i.round_result = 0
                    print("It's a draw")

                elif i.score > dealer_data.score:
                    print(i.name, "win!")
                    win(dealer_data, i, 1)

                elif i.score < dealer_data.score:
                    print(i.name, "loses!")
                    lose(dealer_data, i)
            else:
                print("Dealer busted")
                print(i.name, "win!")
                win(dealer_data, i, 1)
        i.blackjack = 0
        print("\n")

def win(dealer_data, player_data, multiplier):
    winnings = multiplier*player_data.bet_size
    player_data.round_result = winnings
    print(player_data.name, "won $" + str(winnings), "\n")
    player_data.cash += winnings
    dealer_data.cash -= winnings
    player_data.win += 1
    dealer_data.lose += 1
    player_data.games += 1
    dealer_data.games += 1


def lose(dealer_data, player_data):
    losings = player_data.bet_size
    player_data.round_result = -losings
    print(player_data.name, "lost $" + str(losings), "\n")
    player_data.cash -= losings
    dealer_data.cash += losings
    player_data.lose += 1
    dealer_data.win += 1
    player_data.games += 1
    dealer_data.games += 1

def round_summary(player_data, dealer_data):
    dealer_result = 0
    print("Result of this round\n")
    for i in player_data:
        print(i.name + ": " + str(i.round_result))
        dealer_result -= i.round_result
        i.winnings += i.round_result
        dealer_data.winnings -= i.round_result
        i.blackjack = 0
    print("Dealer:", dealer_result, "\n")

def summary(iteration, player_data, dealer_data):
    for i in player_data:
        i.player_summary()

    dealer_data.dealer_summary(player_num)

def reshuffle(deck):
    deck_count = len(deck)
    shuffle_treshold = 70
    if deck_count <= shuffle_treshold:
        print("Time to reshuffle deck")
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4 * 6
        print("Deck reshuffled")
        random.shuffle(deck)
    else:
        pass

    return deck


def game():
    z = 0
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4 * 6
    while z < iteration:
        z += 1
        print("Round", z, "\n")
        deck = reshuffle(deck)
        deal(dealer_data, player_data, deck)
        display_player_info(player_data)
        display_dealer_info(dealer_data)
        blackjack_result = blackjack(dealer_data, player_data)

        if blackjack_result == 1:
            print("Dealer's Black Jack ends this round\n")
            round_summary(player_data, dealer_data)
            display_cash(dealer_data, player_data)
            continue
        else:
            player_draw(dealer_data, player_data, deck)
            dealer_draw(dealer_data, deck)
            score(dealer_data, player_data)
            round_summary(player_data, dealer_data)
            display_cash(dealer_data, player_data)
    summary(z, player_data, dealer_data)


#variables

player_num = 4
iteration = 10000


if __name__ == "__main__":
    player_list = participants(player_num)
    player_data = set_player_profile(player_list)
    dealer_data = set_dealer_profile()
    game()
