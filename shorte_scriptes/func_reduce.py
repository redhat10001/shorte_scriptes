print('*' * 25)
from functools import reduce

rezor = reduce(lambda x, y: x * y, map(int, input().strip().split()))
print(rezor)
