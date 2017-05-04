from flask import Flask, render_template, redirect

app = Flask(__name__)

COUNTS = {
    "GET": 0,
    "POST": 0,
    "DELETE": 0,
    "PUT": 0
}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/statistics")
def statistic():
    return render_template("statistics.html", counts=COUNTS)


@app.route("/request-counter", methods=["GET"])
def get_counter():
    COUNTS["GET"] += 1
    return redirect("/")


@app.route("/request-counter", methods=["POST"])
def post_counter():
    COUNTS["POST"] += 1
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)