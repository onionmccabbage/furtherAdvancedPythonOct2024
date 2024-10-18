# Here we build a Flask microservice to respond tio HTTP requests to specific routes
from flask import Flask
from flask import render_template

def main():
    '''here is a simple Flask implementation'''
    app = Flask(__name__)
    # we then declare routes for our web server
    @app.route('/') # this is the top level of our server
    def root():
        return 'Welcome'
    @app.route('/hello')
    def hello():
        return '<h3>Hello</h3>'
    # sometimes we need several ways to acess the same content
    @app.route('/info')
    @app.route('/about')
    @app.route('/stuff')
    def generic():
        return 'this is info about stuff'
    # we may pass URL parameters to our routing
    @app.route('/greet') # allow the possibility of no person parameter
    @app.route('/greet/<person>') # <> means read a parameter
    def greet(person='Friend'):
        if person:
            return f'<h3>Welcome {person}'
        else:
            return 'Welcome to tis Flask server'
    # we may return an HTML template
    @app.route('/lunch')
    @app.route('/lunch/<dessert>')
    def lunch(dessert=None):
        return render_template('lunch.html', dessert=dessert)
    # we must remember to start the server
    app.run()

if __name__ == '__main__':
    main()
