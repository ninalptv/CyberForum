import string

text = input("Введите любой текст: ")
text = text.translate(str.maketrans('', '', string.punctuation)).lower()
list_text = text.split()
print(f"Общее количество слов: {len(list_text)}")
print('Частота слов:')
text_dict = {}
for word in set(list_text):
    text_dict[word] = list_text.count(word)
for key, value in text_dict.items():
    frequency = (value * 100)/len(list_text)
    print(f"\n'{key}': {frequency:.0f}% ")
