score = int(input())

"""
A*: 91 and above
A: 75 to 90
B: 60 to 74
C: 50 to 59
D: 35 to 49
E: 20 to 34
U: Below 20
"""


if score >= 91:
    print("A*")
elif score >= 75 and score <= 90:
    print("A")
elif score >= 60 and score <= 74:
    print("B")
elif score >= 50 and score <= 59:
    print("C")
elif score >= 35 and score <= 49:
    print("D")
elif score >= 20 and score <= 34:
    print("E")
else:
    print("U")
