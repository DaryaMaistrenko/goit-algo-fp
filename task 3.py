import heapq


def dijkstra(graph, start):
    # Ініціалізація
    heap = [(0, start)]  # (відстань, вершина)
    distances = {vertex: float("infinity") for vertex in graph}  # Відстані до всіх вершин
    distances[start] = 0  # Відстань до стартової вершини
    visited = set()  # Відвідані вершини

    while heap:
        current_distance, current_vertex = heapq.heappop(heap)

        # Пропускаємо вже відвідані вершини
        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        # Оновлюємо відстані до сусідніх вершин
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            # Якщо знайдена коротша відстань до сусіда
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances


def create_graph():
    # Створення графа у вигляді списку суміжностей
    graph = {
        "A": [("B", 1), ("C", 4)],
        "B": [("A", 1), ("C", 2), ("D", 5)],
        "C": [("A", 4), ("B", 2), ("D", 1)],
        "D": [("B", 5), ("C", 1)],
    }
    return graph


def main():
    graph = create_graph()
    start_vertex = "A"

    # Перевірка, чи існує стартова вершина в графі
    if start_vertex not in graph:
        print(f"Вершина {start_vertex} не знайдена в графі.")
        return

    distances = dijkstra(graph, start_vertex)

    # Виведення відстаней
    for vertex in distances:
        print(f"Відстань від {start_vertex} до {vertex} дорівнює {distances[vertex]}")


if __name__ == "__main__":
    main()
