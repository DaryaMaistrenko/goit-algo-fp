items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}

def greedy_algorithm(items, budget):
    # Обчислення співвідношення калорій до вартості для кожної страви
    ratios = {item: info["calories"] / info["cost"] for item, info in items.items()}

    # Сортування страв за співвідношенням калорій до вартості в спадному порядку
    sorted_items = sorted(ratios.items(), key=lambda x: x[1], reverse=True)

    total_cost = 0
    total_calories = 0
    selected_items = []

    # Вибір страв
    for item, ratio in sorted_items:
        if total_cost + items[item]["cost"] <= budget:
            selected_items.append(item)
            total_cost += items[item]["cost"]
            total_calories += items[item]["calories"]

    return selected_items, total_calories, total_cost


# Приклад використання
budget = 100
selected_items, total_calories, total_cost = greedy_algorithm(items, budget)
print("Жадібний алгоритм")
print("Обрані страви:", selected_items)
print("Загальна калорійність:", total_calories)
print("Загальна вартість:", total_cost)


def dynamic_programming(items, budget):
    # Ініціалізація таблиці для динамічного програмування
    dp = [0] * (budget + 1)
    selected_items = [[] for _ in range(budget + 1)]

    # Динамічне програмування
    for item, info in items.items():
        cost = info["cost"]
        calories = info["calories"]
        for current_budget in range(budget, cost - 1, -1):
            if dp[current_budget - cost] + calories > dp[current_budget]:
                dp[current_budget] = dp[current_budget - cost] + calories
                selected_items[current_budget] = selected_items[current_budget - cost] + [item]

    # Визначення оптимальних страв
    optimal_items = selected_items[budget]
    total_calories = dp[budget]
    total_cost = sum(items[item]["cost"] for item in optimal_items)

    return optimal_items, total_calories, total_cost


# Приклад використання
selected_items, total_calories, total_cost = dynamic_programming(items, budget)
print("Динамічне програмування")
print("Обрані страви:", selected_items)
print("Загальна калорійність:", total_calories)
print("Загальна вартість:", total_cost)
