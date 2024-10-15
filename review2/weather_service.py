import requests # may need to pip install requests

def getWeather(city):
    '''make a call to the weather API and return the results as a complex dictionary'''
    try:
        report = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID=957d663a2296945e39a56609740a2548')
        return report.json() # Python will automatically convert the JSON to an object
    except Exception as err:
        print(err)

if __name__ == '__main__':
    print( getWeather('Genoa') )
    print( getWeather('Galway') )
    print( getWeather('Paris') )