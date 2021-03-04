import matplotlib.pyplot as plt
import scipy.special as spec
import math

def p(Y):
    return 1/Y

def q(Y):
    return (Y-1)/Y

#probability für genau Z mal eine bestimmte Zahl in X trials
def P(X,Y,Z):
    return spec.binom(X,Z) * pow(p(Y),Z) * pow(q(Y),X-Z)

#use Poisson distribution as an approximation to the binomial distribution
def λ(X,Y):
    return X * p(Y)
def P_Poisson(X,Y,Z):
    return math.exp(-λ(X,Y)) * pow(λ(X,Y),Z) / math.factorial(Z)

#cumulative probability Z mal oder öfters eine bestimmte Zahl:
def C(X,Y,Z):
    return sum([P(X,Y,z) for z in range(Z,X+1)])
def C_Poisson(X,Y,Z):
    return sum([P_Poisson(X,Y,z) for z in range(Z,X+1)])

plt.plot([C(100,10,z) for z in range(100)])
plt.plot([C_Poisson(100,10,z) for z in range(100)],"--")

plt.show()
