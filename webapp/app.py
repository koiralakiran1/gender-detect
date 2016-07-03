# Import the Flask Framework
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)
data_location = '../gender-data/genders.csv'


def json_list(data, name):
    found = []
    for d in data:
        named, gender, count = d.strip().split(',')
        if named == name:
            found.append({"name": named, "gender": gender, "count": count})
    return found


def getfile(data_location):
    with open(data_location, 'r') as file:
        data = file.readlines()
    return data


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/api', methods=['GET'])
def api():
    name = request.args.get('name')
    data = getfile(data_location)
    gender_dict = json_list(data, name)
    return jsonify({"list": gender_dict})


@app.route('/search', methods=['POST'])
def search():
    query = request.form['query'].lower()
    data = getfile(data_location)
    gender_dict = json_list(data, query)
    return jsonify({"list": gender_dict})


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)
