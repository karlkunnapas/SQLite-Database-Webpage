from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def cafes():
    if request.method == 'GET':
        url = "http://127.0.0.1:5000/"
        res = requests.get(url)
        api_data = res.json()
        column_names = api_data[0].keys()

        return render_template("table.html", results=api_data, colnames=column_names)
    return None


@app.route('/filtering', methods=['POST'])
def filters():
    times = request.form
    url = f"http://127.0.0.1:5000/open?from={times["From"]}&to={times["To"]}"
    res = requests.get(url)
    api_data = res.json()
    if not api_data:
        return "Unfortunately, none of the cafes are open at the requested time."
    column_names = api_data[0].keys()

    return render_template("table.html", results=api_data, colnames=column_names)


@app.route('/add', methods=['POST'])
def adds_cafe():
    data = request.form
    data = data.to_dict()
    url = "http://127.0.0.1:5000/addcafe"
    res = requests.post(url, json=data)
    res = res.json()
    column_names = res[0].keys()

    return render_template("table.html", results=res, colnames=column_names)


@app.route('/delete', methods=['POST'])
def remove_cafe():
    data = request.form
    data = data.to_dict()
    url = f"http://127.0.0.1:5000/remove/{data["id"]}"
    res = requests.delete(url)
    res = res.json()
    column_names = res[0].keys()

    return render_template("table.html", results=res, colnames=column_names)


@app.route('/change', methods=['POST'])
def changes_cafe():
    data = request.form
    data = data.to_dict()
    url = "http://127.0.0.1:5000/edit"
    res = requests.put(url, json=data)
    res = res.json()
    column_names = res[0].keys()

    return render_template("table.html", results=res, colnames=column_names)


if __name__ == '__main__':
    app.run(port=3000, debug=True)
