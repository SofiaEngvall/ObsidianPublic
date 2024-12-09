from flask import Flask, request, redirect, url_for, render_template
import os

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), "templates"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/parameters")
def hello():

    mystring = request.args.get("mystring", "please add mystring=whatever", type=str)

    no1 = request.args.get("no1", 0, type=int)
    no2 = request.args.get("no2", 0, type=int)

    return str(no1+no2)+" "+mystring

#@app.route('/<name>')
@app.route('/hello/<name>') 
def hello_name(name): 
    print("a little test")
    return 'Hello %s!' % name


@app.route('/admin')  # decorator for route(argument) function
def hello_admin():  # binding to hello_admin call
    return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):  # binding to hello_guest call
    return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':  # dynamic binding of URL to function
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))

if __name__ == "__main__":
    app.run(debug=True)
