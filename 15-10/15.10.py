def function(listA, key, length, char):
    switcher = {#создаем словарь
        "center": "^",#=
        "left": "<",
        "right": ">",
    }
    arg = switcher.get(key)#Возвращает значение из словаря по указанному ключу
    str = ""# создаем строку в которой будет результат 
    for i in listA:#проходим по listA
            str += ('{:'+ char + arg + '%s'%length + '}').format(i)#к строке прибовляем ответ(ответ:char + значение по ключу + (если для подстановки требуется только один аргумент, то значение - сам аргумент) )
            str += '\n'#Красота
    return str
print(function(['E','Y','E'], 'center', 100, '*'))#вызываем функию и передаеем ей значения(список)



strone =('{:!^20}').format('d')
print(strone)