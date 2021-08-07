###### Conditionals and loops ######

# Print all the elements of a list of numbers, each on their own line with a for loop
from urllib.request import urlopen
from bs4 import BeautifulSoup

mylist = [i for i in range(10)]

for i in mylist:
    print(i, end='\n')


########## Basic functions ############

# Create a function which takes in two numbers and multiplies them giving the result

def mult(a, b):
    return a * b


###### Writing simple function to do a mathematical operation ########

# Factorial computation (ie. n!) both with recursive and iterative

def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n - 1)


# looping

def factorial(n):
    temp = 1
    for i in range(1,n + 1):
        temp *= i
    return temp

print(factorial(5))


###### Downloading a webpage ######

# Write code to read in a URL

htmls=['https://www.ebay.co.uk/',"https://www.google.com"]

for ht in htmls:
    html = urlopen(ht)
    soup = BeautifulSoup(html, 'lxml')
    print(soup.title.string)





