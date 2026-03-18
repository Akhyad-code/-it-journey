
## Шаблон для `README.md`

```md
# Day 13 — Text Report Tool

## Что делает этот скрипт
Скрипт читает текстовый файл и создает отчет:
- количество строк
- количество слов
- количество символов

## Файлы
- sample.txt — входной текст
- text_report.py — основной код
- report.txt — готовый отчет

## Как запустить
```bash
python text_report.py


---

## 7. Mini cheatsheet

```python
# создать функцию
def my_function():
    print("Hello")

# вызвать функцию
my_function()

# функция с параметром
def greet(name):
    print("Hi,", name)

greet("Aru")

# функция с return
def add(a, b):
    return a + b

result = add(2, 3)
print(result)

# длина текста
len("hello")

# разделить текст на строки
text.splitlines()

# разделить текст на слова
text.split()

# посчитать букву
text.lower().count("a")