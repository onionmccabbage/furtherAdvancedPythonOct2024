# we may need to pip install flask
# Flask is a microservice that implements a simple web server
# if you need a public-facing server then use Flask with Apache etc. (for security)
# Flask is a lightweight service, it leaves security to others
from flask import Flask
from flask import render_template
from weather import getWeather
import requests

# to make a Flask web server...
app = Flask(__name__) # this is conventional
# we declare 'routes' for our web server (remember web servers talk over HTTP)
@app.route('/') # if anyone arrives at our server tey will be given this outcome
def root():
    return 'Hello and welcome to Flask'
@app.route('/map')
def map():
    return '<h2>Here is a map of Paris in deep snow</h2>'
# we can have multiple ways to access a route
@app.route('/info') # we can handle typos, old links etc.
@app.route('/about')
def about():
    return 'this is info about the stuff'

# we can pass REST parameters (Represent State Transfer)
# e.g. /greet or /greet/Ada or /greet/Ada/Lovelace
@app.route('/greet')
@app.route('/greet/<name>') # the <> indicate a URL parameter
@app.route('/greet/<name>/<sname>')
def greet(name=None, sname=None):
    if name:
        if sname:
            return f'<h3>Greetings {name} {sname}</h3>' # Flask has a micro-syntax
        else:
            return f'<h3>Greetings {name}</h3>'
    else:
        return '<h3>Greetings Earthling<h3>'

# we can build the HTML response
@app.route('/menu')
def menu():
    link1 = '<a href="/">Home</a>'
    link2 = '<a href="/about">About</a>'
    link3 = '<a href="/greet">Greet</a>'
    link4 = '<a href="/map">Map</a>'
    return f'{link1} | {link2} | {link3} | {link4}'

@app.route('/lunch')
@app.route('/lunch/<desert>') # REST
def lunch(desert=None):
    # all Flask templates exist in the 'templates' package
    return render_template('lunch.html', desert=desert) # pass any URL arguments into the template

# we can use our Weather service to return a report
@app.route('/weather') # good idea to rovide a default route
@app.route('/weather/<city>')
def weather(city='Athlone'):
    # call the weather service
    w = getWeather(city)
    return w.encode() # all data aover HTTP must be encoded

@app.route('/swapi')
def swapi():
    # CAREFUL unusually, swapi does NOT support www.
    r = requests.get('https://swapi.dev/api/people/1')
    response_dict = r.json()
    name = response_dict['name']
    return name


if __name__ == '__main__':
    # debug=True will live reload on changes
    app.run(host='127.0.0.1', debug=True)

