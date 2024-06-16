# hse_project

### Инструкция для работы с кодом телеграм бота в pycharm:

1. Откройте папку `tgBot` как корневую в pycharm
```bash
    cd tgBot
```
2. Пропишите команду ниже, чтобы разрешит запуск скрипта для подготовки окружения
    ```bash
    chmod +x setup_project.sh
    ```
3. Пропишите команду ниже, чтобы запустить скрипт для подготовки окружения
    ```bash
    ./setup_project.sh
    ```
    скрипт установит все необходимые библиотеки для запуска telegram бота
4. Возможно Вам придется сменить среду выполнения: Перейдите в `Pycharm` > `Settings` > `Project: tgBot` > `Python Interpreter`> `Add Interpreter`> `Existing` и укажите этот путь: `<путь к проекту>/env/bin/python`

### информация о датасете

Файл с данными

https://disk.yandex.ru/d/Ihh18yf4807QPA

**Работа над даными**
* Из изначального дата сета из lenta.ru мы отобрали новости, принадлежащие толко тем темам, по которым написано более 10000 постов
* Из изначального дата сета были удалены ссылки, поскольку являются излишней информацией
* Из изначального дата сета были удалены тэги, поскольку являются излишней информацией

 **Структура данных:**

0. столбец: id
1. столбец title: Заголовок статьи <str>
2. столбец text: Текст статьи <str>
3. столбец topic: Тема новости <str>, но является категориальный признаком, всего тем: 11
4. столбец date: Дата <str> хранит в себе год месяц и число: 1914/09/16

всего статей: 800975

### План действий:

 **Текущая задача:** "Задча классификации  новостей"

1. **EDA:**
* Соотношение классов
* Распределение по годам
* Распределение кол-ва новостей по дням
* Оценка постобработанного текста

2. **Предобработка текста:**
* Удаление стоп-слов и пунктуации
* Нормализация форм слов (Лематизация)
* Создание n-грамм
* Преобразование текста в числовой формат tf-idf / bert-tokenizer.
* Разделение данных на обучающую и тестовую выборки

3. Работа с ML и DL
* Эксперименты с ML архитектурами
  * Случайный лес
  * Логистическая регрессия
* Тюнинг параметров лучшей модели
* Эксперименты с различными нейро-архитектурами
  * 2х слойный перцептрон на Tf-idf
  * Bert
  * LSTM
* Оценка ошибок

8. Создание UI на основе телеграм бота для работы с моделью
* Создание арихектуры системы
* Создание синхроннного бота
* Добавление асинхронности
* Разворачивание сервиса
