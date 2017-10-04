
from flask import Flask
from flask_mysqldb import MySQL
mysql = MySQL()
app = Flask(__name__)
# My SQL Instance configurations 
# Change the HOST IP and Password to match your instance configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'dadichen'
app.config['MYSQL_DB'] = 'studentbook'
app.config['MYSQL_HOST'] = '35.190.215.53'
mysql.init_app(app)

# The first route to access the webservice from http://external-ip:5000/ 
#@pp.route("/add") this will create a new endpoints that can be accessed using http://external-ip:5000/add
@app.route("/")
def hello(): # Name of the method
    cur = mysql.connection.cursor() #create a connection to the SQL instance
    cur.execute('''SELECT * FROM students''') # execute an SQL statment
    rv = cur.fetchall() #Retreive all rows returend by the SQL statment
    return str(rv)      #Return the data in a string format
if __name__ == "__main__":
        app.run(host='0.0.0.0', port='5000') #Run the flask app at port 5000

@app.route("add")
def hello(): # Name of the method
    cur = mysql.connection.cursor() #create a connection to the SQL instance
    cur.execute('''INSERT INTO students (studentName, email) values ("third  student", "thirdstudent@mydit.ie");
''') # execute an SQL statment

@app.route("update")
def hello(): # Name of the method
    cur = mysql.connection.cursor() #create a connection to the SQL instance
    cur.execute('''UPDATE students SET studentName= "fifth student" WHERE studentName= "first student"''') # execute an SQL statment

@app.route("delete")
def hello(): # Name of the method
    cur = mysql.connection.cursor() #create a connection to the SQL instance
    cur.execute('''DELETE  FROM students WHERE studentName= "second student"''') # execute an SQL statment
