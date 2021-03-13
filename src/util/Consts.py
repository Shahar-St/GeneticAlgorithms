import string

GA_POP_SIZE = 600  # ga population size
GA_MAX_ITER = 200  # maximum iterations
GA_ELITE_RATE = 0.1  # elitism rate
GA_MUTATION_RATE = 0.25  # mutation rate
GA_TARGET = 'Hello world!'

UNWANTED_CHARS = ['\t', '\n', '\x0b', '\x0c', '\r']

ALLOWED_CHARS = [c for c in string.printable if c not in UNWANTED_CHARS]
LOWER_BOUND = 32
UPPER_BOUND = 126


BEST = 0
