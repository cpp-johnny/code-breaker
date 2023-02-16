n = int(input())
sequence = [n]

while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3*n + 1
    sequence.append(n)

# print the sequence as a string with space-separated elements
print(' '.join(str(x) for x in sequence))

"""
In the code above, we first read the input number n from the user, and initialize a list called sequence to contain the sequence of numbers generated by the algorithm.

We then start a loop that continues until the current number n reaches 1. At each iteration of the loop, we check if n is even or odd, and update its value accordingly (according to the algorithm described in the problem statement). We then append the new value of n to the sequence list.

After the loop is finished, we print the sequence as a string, with space-separated elements, using the join() method to convert the list to a string
"""