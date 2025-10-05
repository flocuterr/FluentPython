# lax_coordinates = (33.9425, -118.408056)
# city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
# traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

# for passport in sorted(traveler_ids):
#     print('%s/%s' % passport)
# for country, _ in traveler_ids:
#     print(country)

'''
%`操作符进行格式化时，如果右侧是一个元组（tuple），
那么元组中的每个元素会被视为一个单独的参数，
分别对应字符串中的各个占位符。
'''
import os

t = (20, 8)
print(divmod(*t))
_, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
# print(filename)

metro_areas = [('Tokyo', 'JP', 36.933, (35.689722, 139.691667)), 
               ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)), 
               ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
               ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
                ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),]
# print(f'{'':15} | {'lat.':^9} | {'long.':^9}')
# for name, cc, pop, (lattitude, longitude) in metro_areas:
    # if longitude <= 0:
        # print(f'{name:15} | {lattitude:9.4f} | {longitude:9.4f}')

# named tuple
from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))

# print(tokyo)

# print(City._fields)
print(tokyo._asdict())
print(tokyo._fields)

LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)
print(delhi)
