'''
collections.namedtuple 是 Python 中一个实用的工厂函数，
用于创建简单的不可变数据类。它生成的类具有元组的特性（高效、不可变），
同时支持通过字段名访问数据（类似类的属性），提高了代码可读性。

在Python中，通常使用下划线前缀来表示函数（或变量）是受保护的（protected）或私有的（private）

在Python中，`__getitem__`是一个特殊方法，
用于实现对象的索引操作（如`obj[index]`）、迭代，反向迭代，成员检测
切片操作（如`obj[start:stop:step]`）。
当你为类定义了`__getitem__`方法后，就可以使用这些操作。

'''
import collections
from random import choice

# define one card
Card = collections.namedtuple('Card',['rank','suit'])
# print(Card('7','diamonds'))

class FrenchDeck:
    ranks: list = [str(n) for n in range(2,11)] + list('JQKA')
    suits: list = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards: list = [Card(rank, suit) for suit in self.suits 
                      for rank in self.ranks]
        
    def __len__(self) -> int:
        return len(self._cards)
    
    def __getitem__(self, position):
        # print('CHOICING......')
        return self._cards[position]
    
deck = FrenchDeck()
# 自动调用__getitem__
'''
A[用户调用 deck[5]] --> B[Deck.__getitem__(5)]
B --> C[委托给 self._cards[5]]
C --> D[返回列表中的第6张牌]
'''
print(deck[1])
# deck[1] = Card(rank=1, suit='diamonds')
# print(deck[:3])
# print(deck[12::13])
''' 从第一个数据开始对比，每对比一次调用一次__getitem__,
若所有不存在匹配数据，返回FALSE，当发现匹配数据时，立即返回True'''
# print(Card('2','spades') in deck)

# suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

# def spades_high(card):
#     rank_value = FrenchDeck.ranks.index(card.rank)
#     return rank_value * len(suit_values) + suit_values[card.suit]

# for card in sorted(deck, key=spades_high):
#     print(card)

print(deck.__len__())
print(len(deck))