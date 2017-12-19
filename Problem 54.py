poker_dict = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14,'S':1,'H':2,'C':3,'D':4}
royal_flush = [10,11,12,13,14]
hands = {'royal_flush':10, 'straight_flush':9, 'four_of_a_kind':8, 'full_house':7, 'flush':6, 'straight':5, 'three_of_a_kind':4, 'two_pairs':3, 'one_pair':2, 'high_card':1}
def hand_to_number(h1):
    value = []
    suits = []
    for i in h1:
        value.append(poker_dict[i[0]])
        suits.append(poker_dict[i[1]])
    return value,suits

def consecutive(l1):
    y = sorted(l1)
    for i in range(4):
        if y[i] + 1 == y[i + 1]:
            continue
        else:
            return False
    return True

def is_royal_flush(h1):
    if is_flush(h1) and set(h1[0]) == set(royal_flush):
        return True

def is_straight_flush(h1):
    if is_flush(h1) and consecutive(h1[0]):
        return True

def is_flush(h1):
    if h1[1].count((h1[1])[0]) == 5:
        return True

def is_straight(h1):
    if consecutive(h1[0]):
        return True

def is_four_of_a_kind(h1):
    for i in list(set(h1[0])):
        if h1[0].count(i) == 4:
            return True
        else:
            continue

def four_of_a_kind_value(h1):
    for i in list(set(h1[0])):
        if h1[0].count(i) == 4:
            return i
        else:
            continue

def is_three_of_a_kind(h1):
    for i in list(set(h1[0])):
        if h1[0].count(i) == 3:
            return True
        else:
            continue

def three_of_a_kind_value(h1):
    for i in list(set(h1[0])):
        if h1[0].count(i) == 3:
            return i
        else:
            continue

def is_one_pair(h1):
    for i in list(set(h1[0])):
        if h1[0].count(i) == 2:
            return True
        else:
            continue

def one_pair_value(h1):
    for i in list(set(h1[0])):
        if h1[0].count(i) == 2:
            return i
        else:
            continue

def is_two_pairs(h1):
    l1 = []
    for i in list(set(h1[0])):
        if h1[0].count(i) == 2:
            l1.append(i)
        else:
            continue
    if len(l1) == 2:
        return True

def two_pairs_value(h1):
    l1 = []
    for i in list(set(h1[0])):
        if h1[0].count(i) == 2:
            l1.append(i)
        else:
            continue
    return l1

def is_full_house(h1):
    if is_one_pair(h1) and is_three_of_a_kind(h1):
        return True

def is_high_card(h1):
    if not is_flush(h1) and not is_one_pair(h1) and not is_straight(h1) and not is_two_pairs(h1) and not is_full_house(h1) and not is_royal_flush(h1) and not is_four_of_a_kind(h1) and not is_three_of_a_kind(h1):
        return True

def which_hand(h1):
    if is_royal_flush(h1):
        return 'royal_flush'
    elif is_straight_flush(h1):
        return ['straight_flush',max(h1[0])]
    elif is_four_of_a_kind(h1):
        return ['four_of_a_kind',four_of_a_kind_value(h1)]
    elif is_full_house(h1):
        return ['full_house',three_of_a_kind_value(h1),one_pair_value(h1)]
    elif is_flush(h1):
        return ['flush',max(h1[0])]
    elif is_straight(h1):
        return ['straight',max(h1[0])]
    elif is_three_of_a_kind(h1):
        return ['three_of_a_kind',three_of_a_kind_value(h1)]
    elif is_two_pairs(h1):
        return ['two_pairs',two_pairs_value(h1)]
    elif is_one_pair(h1):
        return ['one_pair',one_pair_value(h1)]
    elif is_high_card(h1):
        return ['high_card',max(h1[0])]

def who_wins(h1,h2):
    a = which_hand(h1)
    b = which_hand(h2)
    x = hands[a[0]]
    y = hands[b[0]]
    if x > y:
        return 'p1'
    elif x < y:
        return 'p2'
    else:
        if a[0] == 'full_house':
            if a[0][1] > b[0][1]:
                return 'p1'
            elif a[0][1] < b[0][1]:
                return 'p2'
        else:
            if a[1] > b[1]:
                return 'p1'
            elif a[1] < b[1]:
                return 'p2'

def load_file(filename):
    f = open(filename, "r")
    return f.readlines()

c = 0
for i in load_file("p054_poker.txt"):
    a = i.split()[0:5]
    b = i.split()[5:10]
    x = hand_to_number(a)
    y = hand_to_number(b)
    if (who_wins(x,y)) == 'p1':
        c += 1
    else:
        continue
print(c)
