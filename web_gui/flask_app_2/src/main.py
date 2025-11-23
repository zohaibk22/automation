from flask import Flask, render_template, request

app = Flask(__name__)
#contains string that contains thr string of the curernt module


@app.route('/', methods = ["GET"])
def index_route():
    return render_template("index.html", output=None, height='', width='', length='')


@app.route("/", methods=["POST"])
def index():
    height = float(request.form.get('height'))
    width = float(request.form.get('width'))
    length = float(request.form.get('length'))

    volume = height * width * length
    return render_template("index.html", output=volume, height=height, width=width, length=length)

if __name__ == "__main__":
    app.run(debug=True)