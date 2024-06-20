import random
from foo_bar_baz import screening
if __name__ == '__main__':
    rndm = random.randint(1,50)
    print(rndm, "is", end = '')
    screening(rndm)
