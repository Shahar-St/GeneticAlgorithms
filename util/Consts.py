import string

import psutil

GA_POP_SIZE = 600  # ga population size
GA_MAX_ITER = 300  # maximum iterations

CLOCK_RATE = psutil.cpu_freq().current * (2 ** 20)  # clock ticks per second

GA_TARGET = 'Hello world!'

UNWANTED_CHARS = ('\t', '\n', '\x0b', '\x0c', '\r')

ALLOWED_CHARS = tuple(c for c in string.printable if c not in UNWANTED_CHARS)
LOWER_BOUND = 32
UPPER_BOUND = 126

BEST = 0

'''------------------DEFAULT_PARSER-------------------'''

DEFAULT_ALGORITHM = 'GeneticAlgorithm'
DEFAULT_CROSSOVER = 'SinglePointCrossover'
DEFAULT_FITNESS = 'AsciiDistance'
DEFAULT_PROBLEM = 'StringMatching'

'''------------------ALLOWED_NAMED_PARSER-------------------'''

ALLOWED_ALGO_NAMES = ('GeneticAlgorithm', 'PSO')
ALLOWED_CROSS_NAMES = ('SinglePointCrossover', 'UniformPointCrossover', 'TowPointCrossover')
ALLOWED_FITNESS_NAMES = ('AsciiDistance', 'BullsAndCows')
ALLOWED_PROBLEM_NAMES = ('StringMatching', 'NQueens')

'''------------------GA-------------------'''
GA_ELITE_RATE = 0.1  # elitism rate
GA_MUTATION_RATE = 0.25  # mutation rate
GA_CONTINUATION_RATE = 0.5

'''------------------PSO------------------'''
COGNITIVE_WEIGHT = 2
SOCIAL_WEIGHT = 2
