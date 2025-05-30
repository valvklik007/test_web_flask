# 🌦 Flask Weather App

Веб-приложение для отображения прогноза погоды по городам с автодополнением и сохранением истории запросов. Для тест задания

## 🚀 Как запустить

Требуется установленный **Docker** и **Docker Compose**.

```bash
git clone https://github.com/valvklik007/test_web_flask.git
cd test_web_flask
docker-compose up --build
```
После запуска откройте в браузере: http://localhost:5000

✅ Реализовано

- [x] Поиск погоды по городу с использованием Weather API
- [x] Автодополнение городов при вводе (с локальным JSON-списком)
- [x] Сохранение истории поиска по IP-адресу
- [x] API: отображение статистики по количеству запросов на каждый город
- [x] При повторном посещении сайта отображается последний искомый город
- [x] Приложение упаковано в Docker-контейнер

## Запрос статистики API
```
http://localhost:5000/api/stats
```
Ответ в json формате:
```json
[
  {
    "city": "Москва",
    "count": 5
  },
  {
    "city": "Санкт-Петербург",
    "count": 3
  }
]
```

## 📚 Использовалось
```
1. Flsk
2. Flask-wtf
3. Sqlalchemy
4. Flask-Migrate
5. SQLite
```
