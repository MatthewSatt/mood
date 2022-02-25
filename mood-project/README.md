Welcome to mood!

mood is an application that allows users to store and organize their mp3 and mp4 songs.

Getting Started
To view and use this application, you can either navigate to the live hosted site and login as a new or demo user, or download the project locally:

Clone this repository https://github.com/MatthewSatt/mood.git

Install dependencies in the main project folder pipenv install

cd into /react-app and install dependencies npm install

Create a .env file based on the .env.example given

Setup a PostgresSQL user + database in /python-project

psql -c "CREATE USER <username> PASSWORD '<password>' CREATEDB"
psql -c "CREATE DATABASE <database name> WITH OWNER <username>"
Start shell + migrate database + seed database + run flask in the main folder

pipenv shell
flask db upgrade
flask db migrate
flask db seed all
flask run
Keeping flask running, start the app by running npm start in /react-app

Enjoy!
