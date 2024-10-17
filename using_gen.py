# Python offers range() and comprehensions
r = range(0,33,2)
# a range exists in memory, but its generated values are generated on demand (they do not persist in memory)
print(r, type(r))

# a comprehension
e = [i for i in range(0,100, 2)] # a list (in memory)
f = (i for i in range(1, 101, 2))# a generator (the values do not exist in memory)
print(e, type(e))
print(f, type(f))
# we may draw values from a generator
print(f.__next__()) # 1
print(f.__next__()) # 3
print(f.__next__()) # 5
for _ in f:
    print(_, end=', ')

# we can declare our own custom generator
def tally(incr=1, maxi=False):
    '''This generator will yield an endless tally of values'''
    score = 0
    try:
        while True:
            yield score # by using yield we have a generator
            score += incr
            if maxi and score > maxi:
                raise StopIteration # this is the correct way to end a generator
    except StopIteration as e:
        pass
        
if __name__ == '__main__':
    game = tally(5, 95)
    print(game, type(game))
    print( game.__next__() ) # 0
    print( game.__next__() ) # 5
    print( game.__next__() ) # 10
    for _ in game:
        print(_, end = ', ')