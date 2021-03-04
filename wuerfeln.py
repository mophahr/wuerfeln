import matplotlib.pyplot as plt
import scipy.special as spec

def p(Y):
    return 1/Y

def q(Y):
    return (Y-1)/Y

#probability für genau Z mal eine bestimmte Zahl in X trials
def P(X,Y,Z):
    return spec.binom(X,Z) * pow(p(Y),Z) * pow(q(Y),X-Z)

#cummulative probability Z mal oder öfters eine bestimmte Zahl:
def C(X,Y,Z):
    return sum([P(X,Y,z) for z in range(Z,X+1)])

plt.plot([C(100,10,z) for z in range(100)])
plt.show()
