import json

# Чтение данных из JSON-файла bd.json
with open('bd.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Вывод данных
print(data)
