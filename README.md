# Реализован "паук" на scrapy для парсинга Steam

## Функционал паука:
- Выбирается 3 запроса по Steam
- Парсятся все игры по каждому запросу по первым двум страницам

Для каждой игры достаются следующие параметры:
- Название
- Категорию (весь путь, за исключением Все игры и самого названия игры)
- Число всех обзоров и общая оценка
- Дата выхода
- Разработчик
- Метки (тэги) игры
- Цена
- Доступные платформы

Результат записывается в json файл, вот пример работы "паука" для запросов: 'cs', 'racing', 'anime' - [par1.json](https://github.com/t1ps9/parsing_steam/blob/main/par1.json)