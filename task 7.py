import random
import matplotlib.pyplot as plt


def simulate_dice_rolls(num_simulations):
    sum_counts = {i: 0 for i in range(2, 13)}

    for _ in range(num_simulations):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        result_sum = die1 + die2
        sum_counts[result_sum] += 1

    probabilities = {s: count / num_simulations for s, count in sum_counts.items()}
    probabilities_percent = {s: p * 100 for s, p in probabilities.items()}

    return probabilities_percent


def plot_probabilities(probabilities_percent):
    sums = list(probabilities_percent.keys())
    probs = list(probabilities_percent.values())

    plt.figure(figsize=(10, 6))
    plt.bar(sums, probs, color="skyblue")
    plt.xlabel("Сума")
    plt.ylabel("Ймовірність (%)")
    plt.title("Ймовірності кожної суми при киданні двох кубиків")
    plt.xticks(sums)
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    # Додавання теоретичних ймовірностей для порівняння
    theoretical_probs = {2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36,
                         7: 6/36, 8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36}
    theoretical_probs_percent = {s: p * 100 for s, p in theoretical_probs.items()}
    plt.plot(sums, [theoretical_probs_percent[s] for s in sums], color='red', marker='o', label='Теоретичні ймовірності')
    
    plt.legend()
    plt.show()


def main():
    num_simulations = 100000  # Можна дозволити користувачеві вводити цю величину
    probabilities_percent = simulate_dice_rolls(num_simulations)

    print("Ймовірності кожної суми (у відсотках):")
    for s, p in probabilities_percent.items():
        print(f"Сума {s}: {p:.2f}%")

    plot_probabilities(probabilities_percent)


if __name__ == "__main__":
    main()

