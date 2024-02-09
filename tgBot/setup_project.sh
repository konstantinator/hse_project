#!/bin/bash

# Название виртуального окружения
VENV_NAME=env

# Проверка наличия папки виртуального окружения
if [ -d "$VENV_NAME" ]; then
  echo "Виртуальное окружение '$VENV_NAME' уже существует."
else
  # Создание виртуального окружения
  echo "Создание виртуального окружения '$VENV_NAME'..."
  python3 -m venv $VENV_NAME
  echo "Виртуальное окружение '$VENV_NAME' успешно создано."
fi

# Активация виртуального окружения
echo "Активация виртуального окружения '$VENV_NAME'..."
source $VENV_NAME/bin/activate

# Установка зависимостей из файла requirements.txt
if [ -f "requirements.txt" ]; then
  echo "Установка зависимостей из файла requirements.txt..."
  pip install -r requirements.txt
  echo "Зависимости успешно установлены."
else
  echo "Файл requirements.txt не найден. Пропуск установки зависимостей."
fi

# Скачивание данных
curl -L $(yadisk-direct https://disk.yandex.ru/d/Ihh18yf4807QPA) -o data.zip
curl -L $(https://disk.yandex.ru/d/OfkV_Ar_1jCIAA) -o models.zip

# Распаковка данных
unzip data.zip
unzip models.zip

# Удаление архива
rm data.zip
rm models.zip
