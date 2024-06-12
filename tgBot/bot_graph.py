import networkx as nx
import matplotlib.pyplot as plt
from aiogram.fsm.state import StatesGroup, State


class BotStates(StatesGroup):
    registration_state = State()
    main_menu_state = State()           # Главное меню
    choosing_model_state = State()      # Выбор модели
    logreg_state = State()              # Вставка новости для лог рег
    randomforest_state = State()        # Вставка новости для randomForest
    lr_prob_state = State()             # Вывод уверенность logreg своем ответе
    rf_prob_state = State()             # Вывод уверенность randomForest своем ответе
    sim_state = State()                 # Вставка новости для поиска похожей
    rate_state = State()                # Вставка новости для поиска подходящей


G = nx.DiGraph()

# Добавляем узлы и ребра
G.add_edge("Регистрация", "Главное меню")
G.add_edge("Главное меню", "Подбери заголовок")
G.add_edge("Главное меню", "Поиск похожего")
G.add_edge("Главное меню", "Оценка бота")
G.add_edge("Подбери заголовок", "LogReg")
G.add_edge("Подбери заголовок", "RandomForest")
G.add_edge("LogReg", "Уверенность logReg")
G.add_edge("RandomForest", "Уверенность randomForest")

# Визуализация состояний
# Установка позиций узлов
pos = {
    "Регистрация": (0, 5),
    "Главное меню": (0, 4),
    "Подбери заголовок": (-0.75, 3),
    "Поиск похожего": (0, 3),
    "Оценка бота": (1, 3),
    "LogReg": (-1, 2),
    "Уверенность logReg": (-1, 1),
    "RandomForest": (-0.5, 2),
    "Уверенность randomForest": (-0.5, 1)
}

fig, ax = plt.subplots(figsize=(12, 6))
nx.draw(G, pos, with_labels=True, node_color='lightblue', font_size=10, arrows=True)
plt.show()

# Словарь для сопоставления человеко-читаемых названий с идентификаторами
node_to_state = {
    "Регистрация": BotStates.registration_state,
    "Главное меню": BotStates.main_menu_state,
    "Подбери заголовок": BotStates.choosing_model_state,
    "LogReg": BotStates.logreg_state,
    "Уверенность logReg": BotStates.lr_prob_state,
    "RandomForest": BotStates.randomforest_state,
    "Уверенность randomForest": BotStates.rf_prob_state,
    "Поиск похожего": BotStates.sim_state,
    "Оценка бота": BotStates.rate_state
}


class GraphNavigator:
    def __init__(self, graph, node):
        self.graph = graph
        self.current_node = node

    def move_to_node(self, node):
        if node in self.graph:
            self.current_node = node

    def get_parent(self):
        if self.current_node == "Регистрация":
            return "Регистрация"
        parent = list(self.graph.predecessors(self.current_node))[0]
        return parent

    def move_to_parent(self):
        self.current_node = self.get_parent()

    def get_current_node(self):
        return self.current_node
