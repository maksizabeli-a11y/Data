# Тестовый скрипт для проверки модуля DataProcessor
from DataProcessor import DataProcessor

# Создание экземпляра процессора
processor = DataProcessor()
print("=== Тестирование DataProcessor ===\n")

# 1. Тест добавления чисел
print("1. Добавление чисел:")
processor.add_number(10)
processor.add_number(25)
processor.add_number(7)
print(f"   Добавлены числа: 10, 25, 7")
print(f"   Текущие данные: {processor.data}\n")

# 2. Тест добавления строк
print("2. Добавление строк:")
processor.add_text("Привет")
processor.add_text("Мир")
processor.add_text("Конференция")
print(f"   Добавлены строки: 'Привет', 'Мир', 'Конференция'")
print(f"   Текущие данные: {processor.data}\n")

# 3. Тест получения суммы чисел
print("3. Получение суммы чисел:")
total = processor.get_sum()
print(f"   Сумма всех чисел: {total}\n")

# 4. Тест получения всех строк
print("4. Получение всех строк:")
texts = processor.get_texts()
print(f"   Найденные строки: {texts}\n")

# 5. Тест смешанных данных
print("5. Тест со смешанными данными:")
processor.add_number(100)
processor.add_text("Тест")
print(f"   Добавлены: число 100 и строка 'Тест'")
print(f"   Все данные: {processor.data}")
print(f"   Сумма чисел: {processor.get_sum()}")
print(f"   Все строки: {processor.get_texts()}")