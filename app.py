from chalice import Chalice
import datetime

app = Chalice(app_name='helloworld')

@app.route('/')
def index():
    return {'Harvard Computer Society FTW!':
            'Bootcamp 3, by Simas Sakenis'}

month_to_int = {'January': 1,
                'February': 2,
                'March': 3,
                'April': 4,
                'May': 5,
                'June': 6,
                'July': 7,
                'August': 8,
                'September': 9,
                'October': 10,
                'November': 11,
                'December': 12}

int_to_month = {1: 'January',
                2: 'February',
                3: 'March',
                4: 'April',
                5: 'May',
                6: 'June',
                7: 'July',
                8: 'August',
                9: 'September',
                10: 'October',
                11: 'November',
                12: 'December',}

weekday = ['Monday',
           'Tuesday',
           'Wednesday',
           'Thursday',
           'Friday',
           'Saturday',
           'Sunday']

def month_int(month):
    try:
        m = int(month)
    except:
        m = month_to_int[month.lower().capitalize()]
    return m

def date_string(year, month, day):
    day_suffix = 'th'
    if day % 10 == 1 and day // 10 != 1: day_suffix = 'st'
    elif day % 10 == 2 and day // 10 != 1: day_suffix = 'nd'
    elif day % 10 == 3 and day // 10 != 1: day_suffix = 'rd'
    return str(day) + day_suffix + ' of ' + int_to_month[month] + ', ' + str(year) + ','

@app.route('/weekday/{year}/{month}/{day}')
def weekday_of_date(year, month, day):
    try:
        y = int(year)
        m = month_int(month)
        d = int(day)
        date = datetime.date(y, m, d)
        return {'The ' + date_string(y, m, d) + ' is...': weekday[date.weekday()] + '!'}
    except:
        return {'This date does not exist...': 'try a different one!'}
