# TalTech Campus Cafes Database (SQLite, Flask)

## Description

Developed as part of an advanced Python course at TalTech, this project creates a SQLite database from a provided CSV file containing campus cafe data. A Flask API interfaces with the database and powers a web app that displays all cafes in a table and includes a form for database interactions via dropdown menu.

To enhance UI/UX, the webpage was styled using CSS and designed with TalTech's official colors and imagery for visual consistency. ChatGPT was used to refine the visual layout.

## Requirements

* Python 3.x
* Flask
* SQLite
* SQLite Studio (optional, for database inspection)

## Running the Application

1. Run the `database.py` script to initialize the SQLite database and Flask app API.
2. Start the webpage Flask app by running `web.py`.
3. Open your browser and go to [http://127.0.0.1:3000](http://127.0.0.1:3000) (also shown in the console as "Running on...").

## Design Choices

The UI uses TalTech's official color palette and background to match the theme of the project.

## Technical Highlights

* SQLite database setup and query handling
* RESTful API development using Flask
* Implementation of HTTP methods (GET, POST, PUT, DELETE)
* Frontend styling and layout enhancements using CSS
