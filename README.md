
# Brand Rating Analyzer

Скрипт читает CSV-файлы с рейтингами товаров и формирует отчёт `average-rating` — средний рейтинг бренда.

## Пример запуска
python3 main.py --files products/products1.csv products/produts2.csv --report average-rating

## Как добавить новый отчёт
Создайте файл в папке `reports/` и зарегистрируйте его в словаре `reports` в `main.py`.
