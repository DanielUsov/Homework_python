import datetime
while True:
    date_ = input('Input DD/MM/YY: ')
    day , month, year = date_.split('/')
    d = int(day)
    m = int(month)
    y = int(year)
    def checkdate(d, m, y):
        if (d == 31):
            if (m != 1, 3, 5, 7, 8, 10, 12):
                print('дата не корректна')
                quit()
        if not(0 < d < 32):
            print('не то')
            quit()
        if not(0 < m < 13):
            print('не то')
            quit()
        if not(y > 0):  
            print('не то')
            quit()
        if not(y < 2021):
            if not(m < 11):
                if not(d < 12):
                    print('не то')
                    quit()
        if (m == 2 and d == 29):
            if y%4 != 0:
                print('дата не корректна')
                quit()

    checkdate(d, m, y)
