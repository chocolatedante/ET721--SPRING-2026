"""
Dante Vanderpool
lab 11, intro to flash 
march 10 2026
"""
from flask import Flask, render_template

"""
create an object 'app' from the Flask module
"""
app = Flask(__name__)

#Set the routing to the main page
#'route' decorator is used to access the root URL
@app.route('/')
def index():
    name= " Dante Vanderpool "
    fruits = ['apple', 'orange', 'grapes']
    fruit ='orange'
    return render_template('index.html', username = name, listfruits = fruits, f = fruit)

#endpoits refer to thr name of the view in an app
@app.route('/about')
def about():
    pics = ['swords.jpeg', 'crystals.jpeg', 'planty.jpeg']
    return render_template('about.html', imagelist = pics)


@app.route('/quotes')
def quotes():
    return '<h1>Quotes</h1>'



#set the 'app' to run if you execute the file directly (not when it is imported)
if __name__ == '__main__':
    app.run(debug=True)
