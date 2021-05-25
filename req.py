import requests


def get_weather(url):
    result = requests.get(url)
    if result.status_code == 200:
        return result.json()
    else:
        print("Something wrong")


if __name__ == '__main__':
    data = get_weather('http://api.openweathermap.org/data/2.5/weather?q=London&units=metric&appid=f24731cd06c0e3d3dfbd1ac9511fbd9b')
    print(data)