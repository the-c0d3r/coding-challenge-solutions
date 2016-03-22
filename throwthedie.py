import random

ran = lambda: random.choice([i for i in range(1,7)])
d1 = ran()
d2 = ran()

print("Die 1 is ",d1)
print("Die 2 is ",d2)
print("Total Number is ",d1+d2)