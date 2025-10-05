# import array
# symbols = '$¢£¥€¤'
# T = tuple(ord(symbol) for symbol in symbols)
# print(T)

# A = array.array('I', (ord(symbol) for symbol in symbols))
# print(A)
# 列表推导一次生成所有元素，将列表存储在内存中，而列表生成器每次会在每次迭代时生成一个组合，从而节省空间。
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in (f'{color} {size}' for color in colors for size in sizes):
    print(tshirt)