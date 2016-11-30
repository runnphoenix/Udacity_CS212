# CS 212, lesson1 - Poker
# -----------------

import itertools  # 注意itertools模块的用法


def hand_rank(hand):
    "Return a value indicating the ranking of a hand."
    groups = group(['--23456789TJQKA'.index(r) for r, s in hand])
    counts, ranks = zip(*groups)
    if ranks == (14, 5, 4, 3, 2):
        ranks = (5, 4, 3, 2, 1)
    straight = len(ranks) == 5 and max(ranks)-min(ranks) == 4
    flush = len(set([s for r, s in hand])) == 1
    return max(count_rankings[counts], 4*straight + 5*flush), ranks  # 注意这里的技巧

count_rankings = {(5,): 10, (4, 1): 7, (3, 2): 6, (3, 1, 1): 3, (2, 2, 1): 2, (2, 1, 1, 1): 1, (1, 1, 1, 1, 1): 0}


def group(ranks):
    return sorted([(ranks.count(x), x) for x in set(ranks)], reverse=True)


def poker(hands):
    return max(hands, key=hand_rank)

print(poker(["7S 2D 9S 4D 5S".split(), "7H 3H 9D 4H JD".split()]))

# Homeworks
# 1
def best_hand(hand):
    return max(itertools.combinations(hand, 5), key=hand_rank)  # key=xx,不是调用,没有括号

# 2
allranks = '23456789TJQKA'
redcards = [r+s for r in allranks for s in 'HD']
blackcards = [r+s for r in allranks for s in 'CS']

def best_wild_hand(hand):
    hands = set(best_hand(set(h)) for h in itertools.product(*map(replacements, hand)))  # Starred Expression 的使用
    return max(hands, key=hand_rank)

def replacements(card):
    if card == '?B':
        return blackcards
    elif card == '?R':
        return redcards
    else:
        return [card]