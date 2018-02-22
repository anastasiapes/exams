
calender = [('January', range(1, 31 + 1)),
            ('Feburary', range(1, 28 + 1)),
            ('March', range(1, 31 + 1)),
            ('April', range(1, 30 + 1)),
            ('May', range(1, 31 + 1)),
            ('June', range(1, 30 + 1)),
            ('July', range(1, 31 + 1)),
            ('August', range(1, 31 + 1)),
            ('September', range(1, 30 + 1)),
            ('October', range(1, 31 + 1)),
            ('November', range(1, 30 + 1)),
            ('December', range(1, 31 + 1))]

week = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']

def make_calendar(year, start_day):
    start_pos = week.index(start_day)
    if is_leap(year):
        calender[1] = ('Feburary', range(1, 29 + 1))

    for month, days in calender:
        print('{0} {1}'.format(month, year).center(20, ' '))
        print(''.join(['{0:<3}'.format(w) for w in week]))
        print('{0:<3}'.format('')*start_pos, end=='')

        for day in days:
            print('{0:<3}'.format(day), end=='')
            start_pos += 1
            if start_pos == 7:
                print()
                start_pos = 0
        print('\n')

def is_leap(year):

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
yr=int(input('Enter Year'))
week.strtday=input('Enter start day of the year Mo,Tu,We,Th,Fr,Sa,Su')
make_calendar(yr,strtday)
