# goit-algo-fp
```python
Покрокова інструкція виконання фінального проєкту

Завдання 1. Структури даних. Сортування. Робота з однозв'язним списком

Для реалізації однозв'язного списку (приклад реалізації можна взяти з конспекту) необхідно:

написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;
розробити алгоритм сортування для однозв'язного списку, наприклад, сортування вставками або злиттям;
написати функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список.

Завдання 2. Рекурсія. Створення фрактала “дерево Піфагора” за допомогою рекурсії

Необхідно написати програму на Python, яка використовує рекурсію для створення фрактала “дерево Піфагора”. Програма має візуалізувати фрактал “дерево Піфагора”, і користувач повинен мати можливість вказати рівень рекурсії.

Завдання 3. Дерева, алгоритм Дейкстри

Розробіть алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі, використовуючи бінарну купу. Завдання включає створення графа, використання піраміди для оптимізації вибору вершин та обчислення найкоротших шляхів від початкової вершини до всіх інших.

Завдання 4. Візуалізація піраміди

Наступний код виконує побудову бінарних дерев. Виконайте аналіз коду, щоб зрозуміти, як він працює.
import uuid

import networkx as nx
import matplotlib.pyplot as plt

class Node:
  def __init__(self, key, color="skyblue"):
    self.left = None
    self.right = None
    self.val = key
    self.color = color # Додатковий аргумент для зберігання кольору вузла
    self.id = str(uuid.uuid4()) # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
  if node is not None:
    graph.add_node(node.id, color=node.color, label=node.val) # Використання id та збереження значення вузла
    if node.left:
      graph.add_edge(node.id, node.left.id)
      l = x - 1 / 2 ** layer
      pos[node.left.id] = (l, y - 1)
      l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
    if node.right:
      graph.add_edge(node.id, node.right.id)
      r = x + 1 / 2 ** layer
      pos[node.right.id] = (r, y - 1)
      r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
  return graph

def draw_tree(tree_root):
  tree = nx.DiGraph()
  pos = {tree_root.id: (0, 0)}
  tree = add_edges(tree, tree_root, pos)

  colors = [node[1]['color'] for node in tree.nodes(data=True)]
  labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} # Використовуйте значення вузла для міток

  plt.figure(figsize=(8, 5))
  nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
  plt.show()

## Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

## Відображення дерева
draw_tree(root) 

Використовуючи як базу цей код, побудуйте функцію, що буде візуалізувати бінарну купу.

 👉🏻 Примітка. Суть завдання полягає у створенні дерева із купи.

Завдання 5. Візуалізація обходу бінарного дерева

Використовуючи код із завдання 4 для побудови бінарного дерева, необхідно створити програму на Python, яка візуалізує обходи дерева: у глибину та в ширину.

Вона повинна відображати кожен крок у вузлах з різними кольорами, використовуючи 16-систему RGB (приклад #1296F0). Кольори вузлів мають змінюватися від темних до світлих відтінків, залежно від послідовності обходу. Кожен вузол при його відвідуванні має отримувати унікальний колір, який візуально відображає порядок обходу.

👉🏻 Примітка. Використовуйте стек та чергу, НЕ рекурсію

Завдання 6. Жадібні алгоритми та динамічне програмування

Необхідно написати програму на Python, яка використовує два підходи — жадібний алгоритм та алгоритм динамічного програмування для розв’язання задачі вибору їжі з найбільшою сумарною калорійністю в межах обмеженого бюджету.

Кожен вид їжі має вказану вартість і калорійність. Дані про їжу представлені у вигляді словника, де ключ — назва страви, а значення — це словник з вартістю та калорійністю.

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

Розробіть функцію greedy_algorithm жадібного алгоритму, яка вибирає страви, максимізуючи співвідношення калорій до вартості, не перевищуючи заданий бюджет.

Для реалізації алгоритму динамічного програмування створіть функцію dynamic_programming, яка обчислює оптимальний набір страв для максимізації калорійності при заданому бюджеті.

Завдання 7. Використання методу Монте-Карло

Необхідно написати програму на Python, яка імітує велику кількість кидків кубиків, обчислює суми чисел, які випадають на кубиках, і визначає ймовірність кожної можливої суми.

Створіть симуляцію, де два кубики кидаються велику кількість разів. Для кожного кидка визначте суму чисел, які випали на обох кубиках. Підрахуйте, скільки разів кожна можлива сума (від 2 до 12) з’являється у процесі симуляції. Використовуючи ці дані, обчисліть імовірність кожної суми.

На основі проведених імітацій створіть таблицю або графік, який відображає ймовірності кожної суми, виявлені за допомогою методу Монте-Карло.

Таблиця ймовірностей сум при киданні двох кубиків виглядає наступним чином.

Порівняйте отримані за допомогою методу Монте-Карло результати з аналітичними розрахунками, наведеними в таблиці вище.

Критерії прийняття фiнального проєкту:

Завдання 1:

- Реалізовано функцію реверсування однозв'язного списку, яка змінює посилання між вузлами. Код виконується.

- Програмно реалізовано алгоритм сортування (функцію) для однозв'язного списку. Код виконується.

- Реалізовано функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список. Код виконується.

Завдання 2:

- Код виконується. Програма візуалізує фрактал “дерево Піфагора”.

- Користувач має можливість вказати рівень рекурсії.

Завдання 3:

- Програмно реалізовано алгоритм Дейкстри для знаходження найкоротшого шляху у графі з використанням бінарної купи (піраміди).

- У межах реалізації завдання створено граф, використано піраміду для оптимізації вибору вершин та виконано обчислення найкоротших шляхів від початкової вершини до всіх інших.

Завдання 4:

- Код виконується. Функція візуалізує бінарну купу.

Завдання 5:

- Програмно реалізовано алгоритми DFS і BFS для візуалізації обходу дерева в глибину та в ширину. Використано стек та чергу.

- Кольори вузлів змінюються від темних до світлих відтінків залежно від порядку обходу.

Завдання 6:

- Програмно реалізовано функцію, яка використовує принцип жадібного алгоритму. Код виконується і повертає назви страв, максимізуючи співвідношення калорій до вартості, не перевищуючи заданий бюджет.

- Програмно реалізовано функцію, яка використовує принцип динамічного

програмування. Код виконується і повертає оптимальний набір страв для максимізації калорійності при заданому бюджеті.

Завдання 7:

- Програмно реалізовано алгоритм для моделювання кидання двох ігрових кубиків і побудови таблиці сум та їх імовірностей за допомогою методу Монте-Карло.

- Код виконується та імітує велику кількість кидків кубиків, обчислює суми чисел, які випадають на кубиках, підраховує, скільки разів кожна можлива сума з’являється у процесі симуляції, і визначає ймовірність кожної можливої суми.

- Створено таблицю або графік, який відображає ймовірності кожної суми, виявлені за допомогою методу Монте-Карло.

- Зроблено висновки щодо правильності розрахунків шляхом порівняння отриманих за допомогою методу Монте-Карло результатів та результатів аналітичних розрахунків. Висновки оформлено у вигляді файлу readme.md фінального завдання.

ВИСНОВКИ:

Завдання 1: Структури даних. Сортування. Робота з однозв'язним списком

Висновки:
- Реалізовано базовий однозв'язний список із можливістю додавання елементів, реверсування списку, сортування вставками та об'єднання двох відсортованих списків.
- Використані алгоритми працюють ефективно для малих обсягів даних, що є достатнім для навчальних цілей.
- Розуміння основних принципів роботи зі структурами даних дозволяє створювати більш складні програми в майбутньому.

Завдання 2: Рекурсія. Створення фрактала “дерево Піфагора”

Висновки:
- Візуалізація фрактала "дерево Піфагора" демонструє практичне застосування рекурсії в графічних програмах.
- Користувач має можливість вказати рівень рекурсії, що дозволяє досліджувати різні варіанти фрактала.
- Програма ілюструє принципи геометрії та самоподібності, що є основою фрактальної геометрії.

Завдання 3: Дерева, алгоритм Дейкстри

Висновки: 
- Реалізовано алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі, що демонструє ефективний підхід до вирішення задач оптимізації.
- Використання бінарної купи (піраміди) для оптимізації вибору вершин підвищує ефективність алгоритму.
- Графічна візуалізація результатів допомагає краще зрозуміти, як працює алгоритм, та його практичні застосування.

Завдання 4: Візуалізація піраміди

Висновки:
- Візуалізація бінарної купи за допомогою бібліотеки networkx і matplotlib дозволяє зрозуміти структуру даних та їх взаємозв'язок.
- Важливість розуміння роботи з графами та деревами підкреслює їх використання в багатьох реальних задачах.
- Код продемонстрував гнучкість візуалізації даних та можливість їх адаптації під конкретні потреби.

![output (1)](https://github.com/user-attachments/assets/ef517bd3-065c-4585-b92a-a1ea6d260ab2)

Завдання 5: Візуалізація обходу бінарного дерева

Висновки:
- Реалізовані алгоритми обходу в ширину (BFS) та в глибину (DFS) на прикладі бінарного дерева показали різні стратегії обробки даних.
- Візуалізація обхідних стратегій з використанням кольорів допомагає ілюструвати принципи обходу та їх ефективність.
- Це завдання поглибило розуміння роботи з деревоподібними структурами та їх практичними застосуваннями в обробці даних.

Завдання 6: Жадібні алгоритми та динамічне програмування

Висновки:
- Розроблено два підходи до задачі вибору їжі з найбільшою сумарною калорійністю в межах бюджету: жадібний алгоритм і динамічне програмування.
- Жадібний алгоритм забезпечує швидке, хоча й не завжди оптимальне рішення, в той час як динамічне програмування гарантує знаходження оптимального набору.
- Це завдання підкреслює важливість вибору алгоритмічного підходу залежно від вимог задачі.

Завдання 7: Використання методу Монте-Карло

Висновки:
- Симуляція кидання двох кубиків за допомогою методу Монте-Карло демонструє потужність статистичних методів для оцінки ймовірностей.
- Порівняння отриманих результатів з аналітичними значеннями підкреслює ефективність та точність методу.
- Візуалізація ймовірностей з використанням графіків покращує розуміння результатів та дає змогу наочно продемонструвати статистичні дані.

## Висновки щодо розрахунків методом Монте-Карло

У цьому завданні ми реалізували симуляцію кидання двох шестигранних кубиків та обчислили ймовірності отримання різних сум (від 2 до 12) за допомогою методу Монте-Карло. Для перевірки точності отриманих результатів ми порівняли їх з аналітичними розрахунками.

## Результати симуляції

Після виконання симуляцій (12 кидків) ми отримали ймовірності для кожної можливої суми:

| Сума | Ймовірність (Монте-Карло) |
|------|-----------------------------|
| 2    | 2.83%                          |
| 3    | 5.39%                          |
| 4    | 8.38%                          |
| 5    | 11.18%                         |
| 6    | 13.84%                         |
| 7    | 16.59%                         |
| 8    | 13.96%	                        |
| 9    | 11.25%                         |
| 10   | 8.34%                          |
| 11   | 5.54%                          |
| 12   | 2.69%                          |

## Аналітичні розрахунки

Згідно з аналітичними підрахунками, ймовірності для кожної суми при киданні двох кубиків розраховуються наступним чином:

| Сума | Ймовірність (Аналітичний розрахунок) |
|------|---------------------------------------|
| 2    | 1/36 (≈ 2.78%)                       |
| 3    | 2/36 (≈ 5.56%)                       |
| 4    | 3/36 (≈ 8.33%)                       |
| 5    | 4/36 (≈ 11.11%)                      |
| ...  | ...                                   |
| 12   | 1/36 (≈ 2.78%)                       |

## Порівняння результатів

При порівнянні отриманих результатів методом Монте-Карло з аналітичними розрахунками ми можемо зробити такі висновки:

1. Точність: 
   - Результати симуляцій виявилися близькими до аналітичних значень, що підтверджує коректність реалізації методу Монте-Карло. 
   - Деякі ймовірності можуть мати невеликі відхилення, що пов'язано з випадковістю та обмеженим числом симуляцій.

2. Відхилення:
   - Як правило, ймовірності, отримані методом Монте-Карло, можуть коливатися навколо аналітичних значень, але з підвищенням кількості симуляцій їх точність зростає.
   - Для досягнення більшої точності рекомендується проводити більше симуляцій.

3. Висновок:
   - Метод Монте-Карло є ефективним інструментом для оцінки ймовірностей у задачах, де аналітичні розрахунки можуть бути складними або неможливими. 
   - У нашому випадку, результати підтверджують, що метод Монте-Карло забезпечує адекватну оцінку ймовірностей при достатній кількості симуляцій.

## Рекомендації

- Для покращення точності результатів рекомендовано проводити більше симуляцій, наприклад, 50 кидків.
- Можливо, доцільно буде візуалізувати отримані результати для кращого сприйняття даних.

