import string
import random

char = string.hexdigits
count = 0
while count <= 1000:
    def pass_generator(size):
        return ''.join(random.choice(char)for _ in range(size))

    result = pass_generator(8)
    print(result)

count += 1