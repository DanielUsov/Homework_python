import random
import string

def randStrok(num):
    new_string = ""
    for i in range(num):
        new_string += random.choice(string.ascii_letters)
    return new_string

def randList(numer1, numer2):
    list = [''] * numer1
    for i in range(numer1):
        for ii in range(numer2):
            list[i] += random.choice(string.ascii_letters)
    return list

def strings(s):
    b = 0; h = 0; j = 0; y = ""
    for i in range(len(s)):
        b = 0; l = 0
        for ii in range(len(s[i])):
            if s[i][ii].isupper():
                b +=1
            else:
                l += 1
        if b > l:
            b +=1
        elif b < l:
            h += 1
        else:
            j += 1
    a= b / (b + h + j) * 100
    c = h / (b + h + j) * 100
    g = j / (b + h + j) * 100
    print('заглавных букв ', a, '%', y)
    print('строчных букв', c, '%', y)
    print('одинаково', g, '%', y )

rand_Strok = randStrok(10)
str(rand_Strok)
rand_list_strok = randList(10, 10)
strings(rand_list_strok)