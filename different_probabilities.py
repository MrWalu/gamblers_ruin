import numpy as np
import matplotlib.pyplot as plt

a = 50
b = 50
c = a + b
p_values = [1/5, 1/2, 4/5]


game_lengths = {p: [] for p in p_values}

for p in p_values:
    for _ in range(100):
        capital_a = a
        capital_b = b
        game_length = 0

        while capital_a > 0 and capital_a < c:
            if np.random.random() < p:
                capital_a += 1
                capital_b -= 1
            else:
                capital_a -= 1
                capital_b += 1
            game_length += 1

        game_lengths[p].append(game_length)
    
    game_lengths[p] = sorted(game_lengths[p])

for p in p_values:
    mean_length = np.mean(game_lengths[p])
    
    if p == 0.2 or p == 0.8:
        plt.hist(game_lengths[p], bins=np.arange(min(game_lengths[p]), max(game_lengths[p]) + 2, 2) - 1, edgecolor='black')
        plt.xlabel('Długość gry')
        plt.ylabel('Liczba gier')
        plt.title(f'Prawdopodobieństwo długości trwania rozgrywki w zależności od p = {p}')
        plt.show()
    else:
        plt.hist(game_lengths[p], bins=np.arange(min(game_lengths[p]), max(game_lengths[p]) + 200, 200) - 1, edgecolor='black')
        plt.xlabel('Długość gry')
        plt.ylabel('Liczba gier')
        plt.title(f'Prawdopodobieństwo długości trwania rozgrywki w zależności od p = {p}')
        plt.show()
    
    print("Prawdopodobieństwo: ", p)
    print("Średnia długość gry: ", mean_length)
    print()