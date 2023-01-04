from audioop import add
from flask import Flask, render_template, url_for, redirect
from cupcakes import get_cupcakes,find_cupcake, add_cupcake_dictionary

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", cupcakes = get_cupcakes("cupcakes.csv"))

@app.route("/cupcakes")
def all_cupcakes():
    return render_template("cupcakes.html", allcupcakes = add_cupcake_dictionary ("cupcakes.csv"))

@app.route("/individual-cupcake")
def individual_cupcake():
    return render_template("individual_cupcake.html", cupcake = find_cupcake("cupcakes.csv", "Chocolate Chip"))

@app.route("/order")
def order():
    return render_template("order.html")

@app.route("/add-cupcake/<name>")
def add_cupcake(name):
    cupcake = find_cupcake("cupcake.csv", name)
    if cupcake:
            add_cupcake_dictionary('orders.csv', cupcake)
            return redirect(url_for("home"))
    else:
            return "sorry cupcake not found."


if __name__ == "__main__":
  
    app.run(debug = True, port = 8000, host = "localhost")