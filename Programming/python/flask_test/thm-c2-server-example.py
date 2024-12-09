from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

app.secret_key = "@09JKD0934jd712?djD"

ADMIN_USERNAME = "admin"           
ADMIN_PASSWORD = "securepassword" #CHANGE ME!!!

@app.route("/")
def home():
    if "logged_in" in session:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session["logged_in"] = True
            session["username"] = username
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html", error="Invalid credentials!")
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "logged_in" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html")

@app.route("/data")
def data():
    if "logged_in" not in session:
        return redirect(url_for("login"))
    return render_template("data.html")

@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    session.pop("username", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)