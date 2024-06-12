# Используем базовый образ с установленным Python
FROM python:3.8-slim

# Устанавливаем зависимости
RUN apt-get update && apt-get install -y \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем spacy и русскую модель
RUN pip install spacy==3.1.3
RUN python -m spacy download ru_core_news_sm

# Устанавливаем FastText
RUN wget https://github.com/facebookresearch/fastText/archive/v0.9.2.zip
RUN unzip v0.9.2.zip && cd fastText-0.9.2 && pip install .

# Копируем файлы проекта в рабочую директорию
WORKDIR /app
COPY . .

# Устанавливаем зависимости проекта
RUN pip install -r requirements.txt

# Команда для запуска бота
CMD ["python", "bot.py"]