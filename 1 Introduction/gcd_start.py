# Find the greatest common denominator of two numbers
# using Euclid's algorithm


def gcd(a, b):
    min = a if a < b else b
    max = a if a != min else b
    denominator = int(min/2)
    while max % denominator != 0 or min % denominator !=0:
        denominator -= 1
    return denominator


    
        
