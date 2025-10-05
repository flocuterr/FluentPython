#----------------------------------------------------------
# 正常方法
# symbols = '$¢£¥€¤'
# code = []

# for symbol in symbols:
#     code.append(ord(symbol))

# print(code)
#---------------------------------------------------------
# 列表推导
symbols = '$¢£¥€¤'
code = [ord(symbol) for symbol in symbols]
print(code)

#利用filter与map实现与列表推导相同的功能
beyond_ascii = [ord(symbol) for symbol in symbols if ord(symbol) > 127]
print(beyond_ascii)

beyond_ascii = list(filter(lambda c: c>127, map(ord, symbols)))
