import json
import os
from datetime import datetime, timedelta

FILE_NAME = 'weather.json'
weather_data = []

def load_data():
    """Загружает данные из JSON-файла."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_data(data):
    """Сохраняет данные в JSON-файл."""
    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def add_record():
    """Добавляет запись за сегодня с указанием температуры и описания."""
    data = load_data()
    
    temperature = float(input("Введите температуру: "))
    description = input("Введите описание погоды: ")
    
    today_str = datetime.today().strftime('%Y-%m-%d')
    
    new_record = {
        "date": today_str,
        "temperature": temperature,
        "description": description
    }
    
    data.append(new_record)
    save_data(data)
    print("Запись добавлена!")

def show_all():
    """Выводит все записи."""
    data = load_data()
    
    print("\n=== Все записи ===")
    for record in data:
        print(f"Дата: {record['date']} | Температура: {record['temperature']}°C | Описание: {record['description']}")

def show_last_week():
    """Выводит записи за последние 7 дней."""
    data = load_data()
    
    today = datetime.today()
    seven_days_ago = today - timedelta(days=7)
    
    print("\n=== Записи за последние 7 дней ===")
    for record in data:
        record_date = datetime.strptime(record['date'], '%Y-%m-%d')
        
        if seven_days_ago <= record_date <= today:
            print(f"Дата: {record['date']} | Температура: {record['temperature']}°C | Описание: {record['description']}")

def show_menu():
    """Показывает меню и обрабатывает выбор пользователя."""
    while True:
        print("\n=== Дневник погоды ===")
        print("1. Добавить запись")
        print("2. Показать все записи")
        print("3. Показать записи за неделю")
        print("0. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == '1':
            add_record()
        elif choice == '2':
            show_all()
        elif choice == '3':
            show_last_week()
        elif choice == '0':
            print("До свидания!")
            break
        else:
            print("Неверный выбор!")

if __name__ == '__main__':
    show_menu()