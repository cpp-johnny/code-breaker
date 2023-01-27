def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a, b = map(int, input().split())
print(gcd(a, b))


"""

This code first defines a function gcd(a, b) that takes two numbers as input and uses a while loop to repeatedly apply the modulus operator (%) to the two numbers. The loop continues until the value of b becomes 0. At that point, the value of a is the GCD of the two input numbers.

The a, b = b, a % b is a multiple assignment. It assigns the value of b to a and the value of a%b to b. This way the values are swapped and the b becomes the new a and a%b becomes the new b.

The next line a, b = map(int, input().split()) takes two space-separated integers as input, convert them to int using the map function and assigns them to the variables a and b.

The last line print(gcd(a, b)) calls the gcd() function with the input values a and b and prints the result.

For the sample input provided the output will be 4.

The Euclidean algorithm is a simple, efficient, and widely used method for finding the GCD of two numbers. It works by repeatedly applying the modulus operator to the two numbers until one of the numbers becomes zero, at which point the other number is the GCD.

The code uses while b because it is based on the Euclidean algorithm, which repeatedly applies the modulus operator (%) to the two input numbers. The goal of the algorithm is to reduce the larger number to zero, and the smaller number will be the greatest common divisor (GCD) of the two input numbers.

The Euclidean algorithm works by swapping the two numbers at each iteration so that the remainder of the division of the larger number by the smaller number becomes the new smaller number, and the previous smaller number becomes the new larger number. The loop continues until one of the numbers becomes zero. At that point, the other number is the GCD of the two input numbers.

In this code, the variable a is being updated with the value of b and b is being updated with the value of a % b. The while loop is checking if b is non-zero, and if it is non-zero the swapping of the values and the modulus operation is done again.

It could also be written as while a but in that case the swapping of the values would be b, a % b and the condition for the while loop would be to check if a is non-zero.

The reason for using b as the condition for the while loop is that it will be the last non-zero value, and thus the GCD.

In short, the choice of using while b or while a is arbitrary and both will work as long as the swapping of the values and modulus operation is done correctly.

"""
