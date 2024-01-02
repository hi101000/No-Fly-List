import random
import namemaker
from pandas import *

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

def make_seed():
    ''' Makes a random string for use as an RNG seed.'''
    n = 30
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join(random.choice(alphabet) for _ in range(n))

def preprocess():
	data = read_csv('nofly.csv')
	fname = data['FIRSTNAME'].tolist()
	mname = data['MIDDLENAME'].tolist()
	lname = data['LASTNAME'].tolist()
	names = []
	print('done')
	l = len(fname)
	printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
	for i, name in enumerate(fname):
		if type(mname[fname.index(name)]) != float:
			names.append(f'{name} {mname[i]} {lname[i]}')
		else:
			names.append(f'{name} {lname[i]}')
		printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
	del fname
	del mname
	del lname
	print('done')
	with open('names.txt', "a") as f:
		for name in names:
			f.write(f'{name}\n')
	print('done')

def main():
    # Seed the random module so we can repeat this game if wanted.
    if seed is None:
        seed = make_seed()
    random.seed(seed)
    namemaker_rng = namemaker.get_rng()         # Since the namemaker module uses its own instance of random.Random,
    namemaker_rng.seed(seed)                    # we have to seed it, too, if we want the name generation to be repeatable.
    print(f'RNG seed: "{seed}"\n')

if __name__ == '__main__':
	preprocess()
