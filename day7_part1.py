import heapq

"""
My original solution then I realised I read how types work completely wrong 
(or rather tried to speed read it and went down some heap solution that was never
gonna work)
"""

f = open("test.txt", "r").readlines()

cards_queue = []

# take advantage of the ordinal code and remap them to how they should be ordered
# in terms of card strength. T is A because it should be the weakest alphabetical ord number here
card_strengths = {"T": "A", "Q": "B", "K": "C", "A": "D", "J": "0"}


def types(hand: str):
    counts = [hand.count(card) for card in hand]

    if 5 in counts:
        return 6
    if 4 in counts:
        return 5
    if 3 in counts:
        if 2 in counts:
            return 4
        return 3
    if counts.count(2) == 4:
        return 2
    if 2 in counts:
        return 1
    return 0


def types_with_j_replacement(hand: str):
    output = []
    all_j_replacements(hand, output)
    return max(map(types, output))


# backtrack
def all_j_replacements(hand: str, output, combo=[]):
    """
            A J K 3 2
            / \  \    \
         1.A  2.J 4.K  5.
              \
           3 AKQT98765432

        1.  2.   3     4  5  6
combo = [A, J, [A..2], K, 3, 2]
    """
    if len(combo) == 5:
        output.append("".join(combo[::]))
        return

    for i in range(len(hand)):
        if hand[i] == "J":
            for c in "AKQT98765432":
                combo.append(c)
                all_j_replacements(hand[i + 1 :], output, combo)
                combo.pop()
        else:
            combo.append(hand[i])
            all_j_replacements(hand[i + 1 :], output, combo)
            combo.pop()


def card_strength(hand: str):
    return (
        types_with_j_replacement(hand),
        [card_strengths.get(card, card) for card in hand],
    )


for line in f:
    hand, bid = line.split()
    heapq.heappush(cards_queue, (card_strength(hand), bid))

total_winnings = 0
rank = 0

while cards_queue:
    item = heapq.heappop(cards_queue)
    bid = int(item[1])
    rank += 1

    total_winnings += bid * rank

print(total_winnings)
