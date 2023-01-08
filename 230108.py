# coding: utf-8
import math

card_count, per_set_count, shuffle_count = map(int, input().split())

card = []
for i in range(card_count):
    card.append(i + 1)

# 切り上げceil
# 四捨五入round
# 切り捨てfloor
set_count = math.ceil(card_count / per_set_count)

for i in range(shuffle_count):
    next_card = []
    for j in range(set_count):
        set_card = []
        for k in range(per_set_count):
            # カード空
            if not card:
                break
            set_card.insert(0, card.pop(0))
        for shuffle_card in set_card:
            next_card.insert(0, shuffle_card)
    card = next_card

for shuffle_card in card:
    print(shuffle_card)


