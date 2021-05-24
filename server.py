from flask import Flask, request
from req import get_weather
from datetime import datetime

city_id = 498817
apikey = 'f24731cd06c0e3d3dfbd1ac9511fbd9b'
app = Flask(__name__)


@app.route('/news')
def news():
    colors = ['green', 'red', 'blue', 'magenta']
    try:
        limit = int(request.args.get('limit'))
    except: limit = 10
    color = request.args.get('color', 'black') if request.args.get('color') in colors else 'black'
    return '<h1 style="color: %s">News: %s</h1>' % (color, limit)


@app.route('/')
def index():
    url = 'http://api.openweathermap.org/data/2.5/weather?id={}&units=metric&appid={}'.format(city_id, apikey)
    weather = get_weather(url)
    date_now = datetime.now().strftime('%d.%m.%Y')

    result = '<p><b>Temperature</b>: %s</p>' % weather['main']['temp']
    result += '<p><b>City</b>: %s</p>' % weather['name']
    result += '<p><b>Date</b>: %s</p>' % date_now

    return result


if __name__ == '__main__':
    app.run(debug=True)
