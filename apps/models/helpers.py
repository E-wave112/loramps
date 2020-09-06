from os import urandom
import random

def generate_code(size):
    random.seed(urandom(16))
    alphabets = [chr(x) for x in range(65, 90)]
    numbers = [chr(x) for x in range(48, 58)]
    code = ''
    for _ in range(size):
        query_set = random.choice((alphabets, numbers))
        code += random.choice(query_set)

    return code