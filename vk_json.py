import json
from random import randint

str_json = """
{
    "response": {
        "count": 32363,
        "items": [{
            "id": 287350527,
            "first_name": "Sonya",
            "last_name": "Kargina"
        }, {
            "id": 341523166,
            "first_name": "Slava",
            "last_name": "Kholod"
        }]
    }
}"""

# Десериализация
data = json.loads(str_json)
items = [i for i in data['response']['items']]

for i in items:
    i['likes'] = randint(50, 200)

# Наглядное отображение через сериализацию
new_json = json.dumps(data, indent=2)
print(new_json)

# Сохранение обработанного файла в json
with open('my_json', 'w') as fd:
    json.dump(data, fd, indent=2)

# Чтение сохраненного файла json
with open('my_json', 'r') as fd:
    data2 = json.load(fd)

# Наглядное отображение считанного файла через сериализацию
print(json.dumps(data2, indent=2))