import numpy as np
import matplotlib.pyplot as plt

a_values = np.arange(1, 101)
b = 100 - a_values
p = 0.5

results = {a: [] for a in a_values}
results_analitics = {a: [] for a in a_values}
def ruin_analitics(a, b):
    ruin_A_prob = b/(a+b)
    return ruin_A_prob

for a in a_values:
    for _ in range(100):
        a_ruin = False
        capital_a = a
        capital_b = 100 - a

        while capital_a > 0 and capital_a < 100:
            if np.random.random() < p:
                capital_a += 1
                capital_b -= 1
                ruin_a_prob = b/(a+b)
            else:
                capital_a -= 1
                capital_b += 1
                ruin_a_prob = b/(a+b)
            
            if capital_a == 0:
                a_ruin = True
                break

        results[a].append(a_ruin)
        results_analitics[a].append(ruin_a_prob)

average_results = {a: np.mean(result) for a, result in results.items()}
a_values = list(average_results.keys())
ruin_probabilities = list(average_results.values())
avg_analitics = {a: np.mean(res) for a, res in results_analitics.items()}
a_val = list(avg_analitics.keys())
ruin_an = list(avg_analitics.values())

plt.plot(a_values, ruin_probabilities)
plt.plot(a_val, ruin_an)
plt.title("Prawdopodobieństwo ruiny gracza A w zależności od początkowego kapitału gracza A")
plt.xlabel("Początkowy kapitał gracza A")
plt.ylabel("Prawdopodobieństwo ruiny gracza A")
plt.grid(True)

plt.show()