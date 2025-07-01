import random

def get_prime():
    Random=random.randint(100,1400)
    for i in range(2,1500):
        monitor=True
        for j in range(2,i):
            if i%j ==0:
                monitor=False
        if monitor and i > Random:
            return i
def GCD(e,phi):
    for i in range(2,phi):
        if e%i == 0 and phi%i==0:
            return False
    return True

