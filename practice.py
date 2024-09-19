print("hello world")

# LAMBDA FUNCTION:-
def add(x,y):
    print("adding two number")
    return x+y


# ITERTOOLS
from itertools import accumulate
data = [1,2,3,4,5]
print(list(accumulate(data)))

from itertools import combinations
data = [1,2,3,4,5]
print(list(combinations(data,2)))

from itertools import groupby
data = [('apple', 1), ('banana', 2), ('apple', 3), ('banana', 4), ('apple', 5)]
for key, value in groupby(data,lambda x:x[0]):
    print(key,list(value))

# COLLECTIONS

from collections import Counter
my_list="aaaaaaaaaaabbbbbbbbbbbbbbbbcccccccccccccccccccddddddddddddddddddddddddddddddddddddddeeeeeeeeeeeeeeeee"
my_Counter = Counter(my_list)
print(my_Counter)
print()

from collections import namedtuple
data = namedtuple('data',['x','y'])
p = data(10,20)
print(p.x)
print(p.y)

from collections import OrderedDict
data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(data)

from collections import deque
d = deque(['a','b','c'])
d.append('d')
d.appendleft('e')
print(d)

