def p():
    d = {}
    while True:
        b = input('Имя:')
        if b == 'q':
            print(d)
            break
        else:
            a = str(input('Номер:'))
            if len(a) == 16:    
                if (a[3:6] + a[7:10] + a[11:13] + a[14:16]).isdigit():
                    if a[0] != "+" and a[1] != "7" and a[2] != "-" and a[6] != "-" and a[10] != "-" and a[13] != "-":
                        print("Ошибка")
                        break       
                else:
                    print("Ошибка")
                    break
            else:
                print("Ошибка")
                break
            d[b] = a
        print(d)    
    return 0
p()