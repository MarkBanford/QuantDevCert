import random

print(random.randint(2, 10))
print(random.random())  # Generate a random float between 0 and 1
print(random.uniform(1, 12))  # Generate a random float between 1 and 12 using a uniform distribution
print(
    random.normalvariate(0, 1))  # Generate a random float from the normal distribution (with a mean of 0 and vol of 1)
