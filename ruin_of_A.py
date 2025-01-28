import numpy as np
import matplotlib.pyplot as plt

def ruin_simulation(a, b, p, num_simulations=100):
    ruin_count_a = 0
    
    for _ in range(num_simulations):
        a_capital, b_capital = a, b
        
        while a_capital > 0 and b_capital > 0:
            if np.random.rand() < p:
                #player A wins
                a_capital += 1
                b_capital -= 1
            else:
                #player B wins
                a_capital -= 1
                b_capital += 1
        
        if a_capital == 0:
            ruin_count_a += 1
    
    return ruin_count_a / num_simulations

def ruin_analitics(a, b, p1):
    p = p1
    q = 1-p
    if p1 == 0.5:
        ruin_A_prob = b/(a+b)
    else:
        dep = q/p #dependency
        ruin_A_prob = (dep**a-dep**(a+b))/(1-dep**(a+b))
    return ruin_A_prob

a_initial = 50
b_initial = 50
p_values = np.linspace(0, 1, 100)
ruin_probabilities = []
ruin_an = []

for p in p_values:
    ruin_prob = ruin_simulation(a_initial, b_initial, p)
    ruin_probabilities.append(ruin_prob)
    an_prob = ruin_analitics(a_initial, b_initial, p)
    ruin_an.append(an_prob)

# Wykres
plt.plot(p_values, ruin_probabilities)
plt.plot(p_values, ruin_an)
plt.xlabel('Probability p')
plt.ylabel("Probability of gambler A's ruin")
plt.title("Dependency of probability of gambler's A ruin to p")
plt.grid(True)
plt.show()
