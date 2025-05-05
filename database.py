import csv
import sqlite3
from flask import Flask, jsonify, request


app = Flask(__name__)
app.json.sort_keys = False


def open_database():
    """
    Create a connection to the database for further actions with the database.
    """
    global connection
    connection = sqlite3.connect('CAFES.db')


def create_database():
    """
    Create a database table "TALTECH" with defined columns.
    """
    # the next line should be uncommented, if it is wanted to create the same table again
    # connection.execute('''DROP TABLE TALTECH''')
    connection.execute('''CREATE TABLE TALTECH
             (ID INTEGER PRIMARY KEY,
             NAME           TEXT     NOT NULL,
             LOCATION       TEXT     NOT NULL,
             OPEN           TEXT     NOT NULL,
             CLOSE          TEXT     NOT NULL);''')
    print("Table created successfully")


def insert_data():
    """
    Insert data line by line into the database from a provided csv file.
    """
    with open("cafes.csv", "r", encoding="UTF-8") as file:
        fieldnames = ["name", "location", "company", "time_open", "time_closed"]
        csv_reader = csv.DictReader(file, fieldnames=fieldnames, delimiter=",")
        data = list(csv_reader)

    for place in data:
        connection.execute(f"INSERT INTO TALTECH (ID,NAME,LOCATION,OPEN,CLOSE) \
                         VALUES (NULL, \"{place["name"]}\", \"{place["location"]}\", \"{place["time_open"]}\", \"{place["time_closed"]}\")")

    connection.commit()


def close_database():
    """
    Close connection to the database.
    """
    connection.close()


@app.route('/', methods=['GET'])
def get_cafes():
    open_database()
    cafes = []
    cursor = connection.execute("SELECT ID,NAME,LOCATION,OPEN,CLOSE from TALTECH")
    for cafe in cursor:
        cafes.append({"ID": cafe[0], "Name": cafe[1], "Location": cafe[2], "Open": cafe[3], "Close": cafe[4]})
    close_database()
    return jsonify(cafes)


@app.route('/open', methods=['GET'])
def get_cafes_open():
    time_from = request.args.get('from', type=str)
    time_to = request.args.get('to', type=str)
    from_h = time_from[:2]
    from_m = time_from[3:]
    to_h = time_to[:2]
    to_m = time_to[3:]
    open_database()
    cafes = []
    cursor = connection.execute(f"SELECT ID,NAME,LOCATION,OPEN,CLOSE from TALTECH where (SUBSTR(CLOSE, 1, 2) > \"{to_h}\" OR SUBSTR(CLOSE, 1, 2) == \"{to_h}\" AND SUBSTR(CLOSE, 4, 5) >= \"{to_m}\") AND (SUBSTR(OPEN, 1, 2) < \"{from_h}\" OR SUBSTR(OPEN, 1, 2) == \"{from_h}\" AND SUBSTR(OPEN, 4, 5) <= \"{from_m}\")")
    for cafe in cursor:
        cafes.append({"ID": cafe[0], "Name": cafe[1], "Location": cafe[2], "Open": cafe[3], "Close": cafe[4]})
    close_database()
    return jsonify(cafes)

@app.route('/addcafe', methods=['POST'])
def new_cafe():
    cafe = request.get_json()

    open_database()
    connection.execute(f"INSERT INTO TALTECH (ID,NAME,LOCATION,OPEN,CLOSE) \
                             VALUES (NULL, \"{cafe["name"]}\", \"{cafe["location"]}\", \"{cafe["open"]}\", \"{cafe["close"]}\")")
    connection.commit()
    close_database()
    return get_cafes()

@app.route('/remove/<id>', methods=['DELETE'])
def del_cafe(id):
    open_database()
    connection.execute(f"DELETE from TALTECH where ID = \"{id}\";")
    connection.commit()
    close_database()
    return get_cafes()

@app.route('/edit', methods=['PUT'])
def change_cafe():
    changed = request.get_json()

    open_database()
    connection.execute(f"UPDATE TALTECH SET NAME = \"{changed["name"]}\", LOCATION = \"{changed["location"]}\", OPEN = \"{changed["open"]}\", CLOSE = \"{changed["close"]}\" WHERE ID = \"{changed["id"]}\";")
    connection.commit()
    close_database()
    return get_cafes()


if __name__ == '__main__':
    app.run(port=5000, debug=True)
    #open_database()
    #create_database()
    #insert_data()
    #close_database()
