import random
from collections import Counter

# 1. Уникальные значения из случайного списка
random_list = [random.randint(1, 20) for _ in range(20)]
unique_values = list(set(random_list))
print(f"1. Исходный список: {random_list}")
print(f"   Уникальные значения: {unique_values}")

print("\n" + "="*50)

# 2. Словарь частот элементов
frequency_dict = {}
for item in random_list:
    frequency_dict[item] = frequency_dict.get(item, 0) + 1
print(f"2. Частотный словарь: {frequency_dict}")

print("\n" + "="*50)

# 3. Множество длинных слов
words_list = ["lion", "tiger", "bear", "wolf", "elephant", "fox", "giraffe"]
long_words = {word for word in words_list if len(word) > 5}
print(f"3. Слова длиннее 5 символов: {long_words}")

print("\n" + "="*50)

# 4. Количество вхождений слов в предложении
sentence = input("4. Введите предложение: ")
word_count = {}
for word in sentence.lower().split():
    # Убираем знаки препинания
    word = word.strip('.,!?;:')
    word_count[word] = word_count.get(word, 0) + 1
print(f"Количество вхождений слов: {word_count}")

print("\n" + "="*50)

# 5. Удаление дубликатов через множество
numbers_with_duplicates = [1, 2, 2, 3, 4, 4, 5, 5, 5]
unique_numbers = list(set(numbers_with_duplicates))
print(f"5. Исходный список: {numbers_with_duplicates}")
print(f"   Без дубликатов: {unique_numbers}")

print("\n" + "="*50)

# 6. Самый дорогой товар
products = {
    "авокадо": 220,
    "папайя": 180,
    "личи": 350,
    "кокос": 190,
    "ананас": 210
}
most_expensive = max(products, key=products.get)
print(f"6. Самый дорогой товар: {most_expensive} ({products[most_expensive]} руб.)")

print("\n" + "="*50)

# 7. Анализ имён
names = ["Гарри", "Гермиона", "Рон", "Драко", "Гарри", "Гермиона", "Гарри"]
name_counter = Counter(names)
repeated_names = [name for name, count in name_counter.items() if count > 1]
most_common = name_counter.most_common(1)[0]

print(f"7. Имена, встречающиеся более раза: {repeated_names}")
print(f"   Самое частое имя: '{most_common[0]}' ({most_common[1]} раз)")

print("\n" + "="*50)

# 8. Словарь первых вхождений символов
text = input("8. Введите строку: ")
first_occurrence = {}
for index, char in enumerate(text):
    if char not in first_occurrence:
        first_occurrence[char] = index

print(f"Словарь первых вхождений: {first_occurrence}")