'''
Input Notation
c : clubs
d : diamonds
h : hearts
s : spades
1 : ace
2 : two
3 : three
4 : four
5 : five
6 : six
7 : seven
8 : eight
9 : nine
10 : ten
11 : jack
12 : queen
13 : king

Format:
    Place suit first, then number for card arrays
    suit_array is alphabetical

Notes:
    Use better return statements (like quads)
    Goal: Try to use any number of cards (preflop, flop, turn, river)
    Problem: Indexing a set number of cards; Solution: Instead of sending in cards array, consider suit array
'''


class community_card:
    def __init__(self, suit, num):
        self.suit = suit
        self.num = num
        # num = str(num)
        self.card = suit, num


class preflop:
    def __init__(self, suit, num):
        self.suit = ""
        self.num = 0
        self.card = suit, num


def preflop_hand(suit1, num1, suit2, num2):
    if suit1 == suit2:
        print("You are suited!")
    if num1 == num2:
        print("You are paired!")
    if num1 == num2 + 1 or num1 == num2 - 1:
        print("You are connected!")


# assign values of 1 or more for numerical cards in play and zeros for cards not in play
def cards_number_array(card1, card2, card3, card4, card5, card6, card7):
    allcards = [card1, card2, card3, card4, card5, card6, card7]
    array = [0] * 14
    for y in range(0, 7):
        array[allcards[y][1]-1] += 1
        if allcards[y][1]-1 == 0:
            array[13] += 1
    return array


# assign values of 1 or more for suit cards in play and zeros for cards not in play
def cards_suit_array(card1, card2, card3, card4, card5, card6, card7):
    allcards = [card1, card2, card3, card4, card5, card6, card7]
    array = [0] * 4
    for y in range(0, 7):
        if allcards[y][0] == 'c':
            array[0] += 1
        if allcards[y][0] == 'd':
            array[1] += 1
        if allcards[y][0] == 'h':
            array[2] += 1
        if allcards[y][0] == 's':
            array[3] += 1
       # array[allcards[y][0]-1] += 1
    print(array)
    return array


def get_card(card_number):
    if card_number == 0 or card_number == 13:
        return "Ace"
    elif card_number == 1:
        return "Two"
    elif card_number == 2:
        return "Three"
    elif card_number == 3:
        return "Four"
    elif card_number == 4:
        return "Five"
    elif card_number == 5:
        return "Six"
    elif card_number == 6:
        return "Seven"
    elif card_number == 7:
        return "Eight"
    elif card_number == 8:
        return "Nine"
    elif card_number == 9:
        return "Ten"
    elif card_number == 10:
        return "Jack"
    elif card_number == 11:
        return "Queen"
    elif card_number == 12:
        return "King"


# consider how we will compare high cards between hands
def check_high_card(array):
    i = 1
    high_card = {}
    for x in range(13, 0, -1):
        if array[x] == 1:
            high_card["rank{0}".format(i)] = x
            i += 1
            if i > 5:
                break
    print(high_card)
  # print(high_card["rank5"])
       # have_high_card = False
       # if have_high_card:
           # print("You have a high card!")
    return True


def check_pair(array):
    pair = False
    for x in range(1, 14):
        if array[x] == 2:
            pair = True
            break
    if pair:
        print("You have a pair!")
    return True


def check_two_pair(array):
    two_pair = False
    number = 0
    for x in range(1, 14):
        if array[x] == 2:
            number += 1
        if number == 2:
            two_pair = True
            break
    if two_pair:
        print("You have two pair!")
    return True


def check_trips(array):
    trips = False
    for x in range(1, 14):
        if array[x] == 3:
            trips = True
            break
    if trips:
        print("You have a trips!")
    return True


def check_straight(array):
    straight = False
    for x in range(0, 14):
        if array[x] >= 1:
            number = 0
            for y in range(0, 5):
                if x+y < 14 and array[x+y] >= 1:
                    number += 1
                else:
                    break
            if number == 5:
                straight = True
                break
    if straight:
        print("You have a straight!")
        return True


def check_flush(array):
    for x in range(0, 7):
        number = 1
        flush = False
        for y in range(0, 7):
            if array[x][0] == array[y][0] and x != y:
                number += 1
            if number == 5:
                print("You have a flush!")
                flush = True
                break
        if flush:
            return True, array[x][0]
    return False, 0


def check_fullhouse(array):
    have_trips = False
    have_pair = False
    for x in range(1, 14):
        if array[x] == 3:
            trips = x
            have_trips = True
            for y in range(1, 14):
                if 1 < array[y] < 4 and y != trips:
                    pair = y
                    have_pair = True
                    break
            if have_pair and have_trips:
                print("You have", get_card(trips) + "s", "full of", get_card(pair) + "s!")
                return True
            else:
                return False


def check_quads(array):
    quads = False
    for x in range(1, 14):
        if array[x] == 4:
            quads = True
            print("You have quads!")
            break
    return quads


def check_straight_flush(array, have_straight, have_flush, suit):
    if have_straight and have_flush:
        # straight_flush = False
        suited_array = [0]*14
        for x in range(0, 7):
            if array[x][0] == suit:
                suited_array[array[x][1]-1] = 1
                if array[x][1] == 1:
                    suited_array[array[x][1] + 12] = 1
        if check_straight(suited_array):

            return True
        else:
            return False


# trying to consider best way to check hand strength
def check_hand_strength():
    # 9 possible hands
    possible_hands = ['High Card', 'Pair', 'Two Pair', 'Trips', 'Straight', 'Flush', 'Full House', 'Quads',
                      'Straight Flush']
    current_hand = None
    if check_high_card(number_array):
        current_hand = possible_hands[0]
    if check_pair(number_array):
        current_hand = possible_hands[1]
    if check_two_pair(number_array):
        current_hand = possible_hands[2]
    if check_trips(number_array):
        current_hand = possible_hands[3]
    straight_boolean = check_straight(number_array)
    if straight_boolean:
        current_hand = possible_hands[4]
    flush_boolean, flush_suit = check_flush(cards_array)
    if check_flush(cards_array)[0]:
        current_hand = possible_hands[5]
    if check_fullhouse(number_array):
        current_hand = possible_hands[6]
    if check_quads(number_array):
        current_hand = possible_hands[7]
    if check_straight_flush(cards_array, straight_boolean, flush_boolean, flush_suit):
        current_hand = possible_hands[8]
        print("You have a straight flush!")
    return current_hand


# Cards in play:
preflop1 = preflop('c', 1)
preflop2 = preflop('c', 9)
flop1 = community_card('d', 10)
flop2 = community_card('d', 11)
flop3 = community_card('d', 12)
turn = community_card('d', 13)
river = community_card('d', 1)
# river = community_card(None, None)
cards_array = preflop1.card, preflop2.card, flop1.card, flop2.card, flop3.card, turn.card, river.card
number_array = cards_number_array(preflop1.card, preflop2.card, flop1.card, flop2.card, flop3.card, turn.card,
                                  river.card)
suit_array = cards_suit_array(preflop1.card, preflop2.card, flop1.card, flop2.card, flop3.card, turn.card, river.card)
preflop_hand(preflop1.card[0], preflop1.card[1], preflop2.card[0], preflop2.card[1])


def main():
    # Functions to check hand combinations:

    check_hand_strength()
'''
    check_high_card(number_array)
    check_pair(number_array)
    check_two_pair(number_array)
    check_trips(number_array)
    straight_boolean = check_straight(number_array)
    flush_boolean, flush_suit = check_flush(cards_array)
    check_quads(number_array)
    check_fullhouse(number_array)
    check_straight_flush(cards_array, straight_boolean, flush_boolean, flush_suit)
'''


if __name__ == "__main__":
    main()










