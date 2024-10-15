import requests # may need to pip install requests

def getWeather(city):
    '''make a call to the weather API
    The weather report is returned as a dictionary'''
    # you can sign up for a free API key (good for 60 requests per minute)
    try:
        report = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID=957d663a2296945e39a56609740a2548')
        return report.json() # Python will convert the JSON into a structure
    except Exception as e:
        print(e)
        
if __name__ == '__main__':
    r = getWeather('Budapest')
    print(r)