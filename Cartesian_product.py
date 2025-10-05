S = ['diammonds', 'hearts', 'clubs', 'spades']
R = ['A', 'K', 'Q']

Caetesian_prod = [rank+suit for rank in R for suit in S]
print(Caetesian_prod)