from flask import Flask, render_template, redirect

app = Flask(__name__)

counts = {
    "GET": 0,
    "POST": 0,
    "DELETE": 0,
    "PUT": 0
}


@app.route("/")
def index():
    global counts
    counts = read_from_file('request_counts.txt')
    return render_template("index.html")


@app.route("/statistics")
def statistic():
    data_to_render = read_from_file('request_counts.txt')
    return render_template("statistics.html", counts=data_to_render)


@app.route("/request-counter", methods=["GET"])
def get_counter():
    global counts
    counts["GET"] = int(counts["GET"]) + 1
    write_to_file(counts, 'request_counts.txt')
    return redirect("/")


@app.route("/request-counter", methods=["POST"])
def post_counter():
    global counts
    counts["POST"] = int(counts["POST"]) + 1
    write_to_file(counts, 'request_counts.txt')
    return redirect("/")


@app.route("/request-counter", methods=["DELETE"])
def delete_counter():
    global counts
    counts["DELETE"] = int(counts["DELETE"]) + 1
    write_to_file(counts, 'request_counts.txt')
    return redirect("/")


@app.route("/request-counter", methods=["PUT"])
def put_counter():
    global counts
    counts["PUT"] = int(counts["PUT"]) + 1
    write_to_file(counts, 'request_counts.txt')
    return redirect("/")


def write_to_file(data, file_name):
    with open(file_name, 'w') as f:
        get_data = 'GET: ' + str(data['GET']) + '\n'
        f.write(get_data)
        get_data = 'POST: ' + str(data['POST']) + '\n'
        f.write(get_data)
        get_data = 'DELETE: ' + str(data['DELETE']) + '\n'
        f.write(get_data)
        get_data = 'PUT: ' + str(data['PUT']) + '\n'
        f.write(get_data)
        return


def read_from_file(file_name):
    with open(file_name, 'r') as f:
        datas = f.readlines()
    results = {}
    results['GET'] = datas[0][5:-1]
    results['POST'] = datas[1][6:-1]
    results['DELETE'] = datas[2][8:-1]
    results['PUT'] = datas[3][5:-1]
    return results

if __name__ == '__main__':
    app.run(debug=True)
