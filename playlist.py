import mysql.connector, os
from flask import Flask, request, render_template, url_for, redirect
from werkzeug.utils import secure_filename
from pygame import mixer


DIR = 'C:\projects\python-playlist-project\music_lib'+'\\'

app = Flask(__name__)
mixer.init()

#when file is uploaded, method saves file to music_lib directory
def create_file_copy():
    file = request.files['path']
    # check if the file has been uploaded
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(DIR, filename))

#creates database and table if database does not exist
def create_database_if_not_exist():
    try:
        py_db_connection = mysql.connector.connect(host="localhost",
                                                   user="root",
                                                   password="password",
                                                   database="temp_db")
        py_db_connection.close()
    except mysql.connector.Error as error:
        py_db = mysql.connector.connect(host="localhost",
                                        user="root",
                                        password="password")
        mycursor = py_db.cursor()
        mycursor.execute("CREATE DATABASE temp_db")
        py_db.close()
        py_db = mysql.connector.connect(host="localhost",
                                        user="root",
                                        password="password",
                                        database="temp_db")
        mycursor = py_db.cursor()
        mycursor.execute("CREATE TABLE mp3_file (id INT NOT NULL AUTO_INCREMENT, filename TEXT NOT NULL, filepathdata TEXT NOT NULL, PRIMARY KEY(id))")
        py_db.close()
        mycursor.close()
        print("Creating temp database")

#Returns connection to mysql database
def connect_to_database():
    try:
        py_db_connection = mysql.connector.connect(host="localhost",
                                        user="root",
                                        password="password",
                                        database="temp_db")
        return py_db_connection
    except mysql.connector.Error as error:
        print("Failed to connect to database")

#disconnects from cursor and database
def disconnect_from_database(connection, cursor):
    if connection.is_connected():
        print("Disconnecting from database")
        connection.close()
        cursor.close()

#returns name of mp3 file
def get_file_name():
    file = request.files['path']
    filename = secure_filename(file.filename)
    return filename

#returns the name of mp3 location
def get_path_name():
    path = request.files['path']
    pathname = secure_filename(path.filename)
    pathname = DIR + pathname
    return pathname

#Inserts data into mysql database
def insertDATA(file, path):
    my_connection = connect_to_database()
    my_cursor = my_connection.cursor()
    mysql_insert_data_query = "INSERT INTO  mp3_file (filename, filepathdata) VALUES (%s, %s)"
    val = (file, path)
    my_cursor.execute(mysql_insert_data_query, val)
    my_connection.commit()
    print("Inserting data to database")
    disconnect_from_database(my_connection, my_cursor)

#returns all data from mp3_file table in mysql database
def get_data_table():
    my_connection = connect_to_database()
    my_cursor = my_connection.cursor()
    mysql_fetch_data_query = "SELECT * FROM mp3_file"
    my_cursor.execute(mysql_fetch_data_query)
    record = my_cursor.fetchall()
    return record

#Stops any currently playing mp3 file and begins playing provided file
def play_sound(path):
    pause_sound()
    mixer.music.load(path)
    mixer.music.play()

#Stops currently playing mp3 file
def pause_sound():
    mixer.music.pause()

#Homepage with list of mp3 file names with play and pause
@app.route('/playlist/', methods=['GET', 'POST'])
def index_form():
    if request.method == 'POST':
        if request.form['submit_button'] == 'play':
            play_sound()
        if request.form['submit_button'] == 'pause':
            pause_sound()
    record = get_data_table()
    return render_template('index.html', value=record)

@app.route('/playlist/playing/<num>', methods=['GET', 'POST'])
def play_form(num):
    file = request.form['hidden']
    play_sound(file)
    record = get_data_table()
    return render_template('index.html', value=record)

@app.route('/playlist/upload', methods=['GET', 'POST'])
def upload_form():
    if request.method == 'POST':
        filename = get_file_name()
        pathname = get_path_name()
        create_file_copy()
        insertDATA(filename, pathname)
    if request.method == 'GET':
        print("GET")
    return render_template('upload.html')

if __name__ == '__main__':
    create_database_if_not_exist()
    app.run(host='localhost', port=8080, debug=True)