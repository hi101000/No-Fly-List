import random
import namemaker
from pandas import *

def make_seed():
    ''' Makes a random string for use as an RNG seed.'''
    n = 30
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join(random.choice(alphabet) for _ in range(n))

def main():
    global names
    # Seed the random module so we can repeat this game if wanted.
    seed = make_seed()
    random.seed(seed)
    namemaker_rng = namemaker.get_rng()         # Since the namemaker module uses its own instance of random.Random,
    namemaker_rng.seed(seed)                    # we have to seed it, too, if we want the name generation to be repeatable.
    print(f'RNG seed: "{seed}"\n')
    names = namemaker.make_name_set('names')
    person = names.make_name()
    print(person)

if __name__ == '__main__':
	main()
