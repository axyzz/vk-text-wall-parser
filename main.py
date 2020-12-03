import vk_api
import json
from math import floor

login, password = 'login', 'password'
vk_session = vk_api.VkApi(login, password)
vk_session.auth(token_only=True)
vk = vk_session.get_api()

x = 1  # Количество записей
id = 1  # id группы или пользователя (ЕСЛИ ID ПРИНАДЛЕЖИТ ГРУППЕ, ОН ДОЛЖЕН НАЧИНАТЬСЯ С -)
dump_to = 'base.json'  # путь к json файлу куда будет производится дамп
i = 0
n = []
while i < x:
    if (x-i)//100 == 0:
        a = vk.wall.get(
            owner_id=id,
            offset=i,
            count=floor(x % 100)
        )
        for s in range(floor(x % 100)):
            n.append(a['items'][s]['text'])
    else:
        a = vk.wall.get(
            owner_id=id,
            offset=i,
            count=100
        )
        for s in range(100):
            n.append(a['items'][s]['text'])
    i += 100
with open('base.json', 'w') as fw:
    json.dump(n, fw)
