import string

def clean_text(words_list):
    result = [] #открываем список
    for word in words_list: #
        has_punctuation_mark = False
        for i in range(len(word)):#от i до длены word
            if word[i] in string.punctuation:
                if i == len(word) - 1:#если i равен длине word
                    new_word = word[:i]
                elif i < len(word):#если i < длины word
                    new_word = word[:i] + word[i + 1:]
                has_punctuation_mark = True
        if not has_punctuation_mark:
            new_word = word
        result.append(new_word.lower())#Добавляет указанный элемент в конец списка.
    print (word)
    return result


def count_words(words_list):
    set_words = set(words_list)#закидываем в множество
    words_dict = {word: words_list.count(word) for word in set_words}#count() возвращает количество вхождений подстроки sub в диапазоне
    return words_dict


def top(words_dict):
    print('Топ 10 слов:')
    items = words_dict.items()#Метод dict.items() возвращает новый список-представление dict_items пар элементов словаря dict, такой как (key, value)
    items = sorted(items, key=lambda x: x[1], reverse=True)
    for word, counter in items[:10]:#выводим слово и кол повторений
        print(word, + counter)


f = open('/home/daniel/text.txt','rt')
s = f.read()
f.close()
ct = clean_text(s.split())#Метод split () в Python разбивает строку на список строк 
top(count_words(ct))