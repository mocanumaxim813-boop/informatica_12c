import random
X=set(random.sample(range(1,200),random.randint(5,20)))
Y=set(random.sample(range(1,200),random.randint(5,20)))
print('(X|Y)=',(X|Y))
print('(X&Y)=',(X&Y))
print(X-Y)
print('(X-Y)|(Y-X)=',(X-Y)|(Y-X))
rint('(X|Y)-(Y|X)=',(X|Y)-(Y|X))