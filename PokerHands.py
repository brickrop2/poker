'''
Input Notation
c : clubs
d : diamonds
h : hearts
s : spades
0, 13 : ace
1 : two
2 : three
3 : four
4 : five
5 : six
6 : seven
7 : eight
8 : nine
9 : ten
10 : jack
11 : queen
12 : king

Format:
    Place suit first, then number for card arrays
    suit_array is alphabetical

Notes:
    right "get" functions if check function is true**
    Consolidate cards_array** Done
    Use better return statements (like quads)** Done
    Important** remove None value from a list without removing the 0 value **solution to below**
    ex: >>> L = [0, 23, 234, 89, None, 0, 35, 9]
    [x for x in L if x is not None]
    [0, 23, 234, 89, 0, 35, 9]
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
def cards_number_array(all_cards):
    array = [0] * 14
    for y in range(0, 7):
        array[all_cards[y][1] - 1] += 1
        if all_cards[y][1]-1 == 0:
            array[13] += 1
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
    return True


def check_pair(array):
    pair = False
    for x in range(1, 14):
        if array[x] == 2:
            pair = True
            break
    return pair


def check_two_pair(array):
    two_pair = False
    number = 0
    for x in range(1, 14):
        if array[x] == 2:
            number += 1
        if number == 2:
            two_pair = True
            break
    return two_pair


def check_trips(array):
    trips = False
    for x in range(1, 14):
        if array[x] == 3:
            trips = True
            break
    return trips


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
    return straight


# assign values of 1 or more for suit cards in play and zeros for cards not in play, returns true if suit >= 5:
def check_flush(all_cards):
    array = [0] * 4
    suits = ['c', 'd', 'h', 's']
    for y in range(0, 7):
        if all_cards[y][0] == 'c':
            array[0] += 1
        elif all_cards[y][0] == 'd':
            array[1] += 1
        elif all_cards[y][0] == 'h':
            array[2] += 1
        elif all_cards[y][0] == 's':
            array[3] += 1
    print(array)
    for x in range(0, 4):
        if array[x] >= 5:
            current_suit = suits[x]
            return True, current_suit
    return False, None


# returns the cards for the flush:
def get_cards_flush(array, suit):
    suited_array = [0] * 14
    for x in range(0, 7):
        if array[x][0] == suit:
            suited_array[array[x][1]-1] = 1
            if array[x][1] == 1:
                suited_array[13] = 1
    i = 1
    high_card = {}
    for y in range(13, 0, -1):
        if suited_array[y] == 1:
            high_card["rank{0}".format(i)] = y
            i += 1
            if i > 5:
                print(i)
                break
    return high_card


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
        return check_straight(suited_array)


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
        get_cards_flush(cards_array, flush_suit)
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
turn = community_card('d', 1)
river = community_card('d', 13)
# river = community_card(None, None)
cards_array = preflop1.card, preflop2.card, flop1.card, flop2.card, flop3.card, turn.card, river.card
# send cards_array into a function, return the array while eliminating None values, and include index # of cards
number_array = cards_number_array(cards_array)
preflop_hand(preflop1.card[0], preflop1.card[1], preflop2.card[0], preflop2.card[1])


def main():
    # Functions to check hand combinations:
    check_hand_strength()


if __name__ == "__main__":
    main()






'''
old code:

# function to find flush
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
    return False, None
    
# function call
    flush_boolean, flush_suit = check_flush(cards_array)

def check_flush(array):
    flush_boolean, flush_suit = cards_suit_array(cards_array)
    if flush_boolean:
        suited_array = [0] * 14
    # needs to cycle through all 7 cards, check suit, if correct suit, write number to suited array (for card number)
        for x in range(0, 7):
            if array[x][0] == flush_suit:
                suited_array[x] = array[x][1]
                print(suited_array[x])
        i = 1
        high_card = {}
        for y in range(13, 0, -1):
            if suited_array[y] == 1:
                high_card["rank{0}".format(i)] = y
                i += 1
                if i > 5:
                    break
        print(high_card)
    return flush_boolean, flush_suit


def cards_suit_array(all_cards):
    array = [0] * 4
    suits = ['c', 'd', 'h', 's']
    for x in range(0, 7):
        if all_cards[x][0] == 'c':
            array[0] += 1
        elif all_cards[x][0] == 'd':
            array[1] += 1
        elif all_cards[x][0] == 'h':
            array[2] += 1
        elif all_cards[x][0] == 's':
            array[3] += 1
    for y in range(0, 4):
        if array[y] >= 5:
            current_suit = suits[y]
            i = 1
            high_card_suited = {}
            for z in range(6, 0, -1):
                if all_cards[z][0] == current_suit:
                    high_card_suited["suited_rank{0}".format(i)] = all_cards[z][1]
                    i += 1
                    print("check")
                    if i > 5:
                        break
    print(high_card_suited)
    print(array)
    return array
'''
