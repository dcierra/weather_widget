import requests
import geocoder
import datetime


API_KEY = ''
HOST = 'https://api.openweathermap.org/data/2.5/'
DAYS = [
    {'number': 0, 'title': 'Понедельник', 'active': False, 'color': '#FFE739', 'order': [0, 1, 2, 3, 4, 5, 6], 'temp': 0, 'type': '-'},
    {'number': 1, 'title': 'Вторник', 'active': False, 'color': '#FFE739', 'order': [1, 2, 3, 4, 5, 6, 0], 'temp': 0, 'type': '-'},
    {'number': 2, 'title': 'Среда', 'active': False, 'color': '#FFE739', 'order': [2, 3, 4, 5, 6, 0, 1], 'temp': 0, 'type': '-'},
    {'number': 3, 'title': 'Четверг', 'active': False, 'color': '#FFE739', 'order': [3, 4, 5, 6, 0, 1, 2], 'temp': 0, 'type': '-'},
    {'number': 4, 'title': 'Пятница', 'active': False, 'color': '#FFE739', 'order': [4, 5, 6, 0, 1, 2, 3], 'temp': 0, 'type': '-'},
    {'number': 5, 'title': 'Суббота', 'active': False, 'color': '#36FF72', 'order': [5, 6, 0, 1, 2, 3, 4], 'temp': 0, 'type': '-'},
    {'number': 6, 'title': 'Воскресенье', 'active': False, 'color': '#36FF72', 'order': [6, 0, 1, 2, 3, 4, 5], 'temp': 0, 'type': '-'}
]


def today():
    geo = geocoder.ip('me')
    lat = geo.lat
    lon = geo.lng
    req = requests.get(f'{HOST}weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric&lang=ru').json()
    result = {
        'city': req['name'],
        'description': req['weather'][0]['description'],
        'temp': int(round(req['main']['temp'])),
        'feels': str(round(req['main']['feels_like'])) + '°C',
        'pressure': str(round(req['main']['pressure'] / 1000 * 750, 2)),
        'wind': req['wind']
    }
    return result


def week():
    today = datetime.datetime.today()
    DAYS[today.weekday()]['active'] = True
    for _ in DAYS:
        if DAYS[today.weekday()]['active']:
            order = DAYS[today.weekday()]['order']
    geo = geocoder.ip('me')
    lat = geo.lat
    lon = geo.lng
    req = requests.get(f'{HOST}onecall?/exclude=daily&lat={lat}&lon={lon}&appid={API_KEY}&units=metric&lang=ru').json()
    result = [DAYS[day] for day in order]
    for el in req['daily']:
        index = req['daily'].index(el)
        if index == 7:
            break
        result[index]['temp'] = round(el['temp']['day'])
        result[index]['type'] = el['weather'][0]['description']
    return result
