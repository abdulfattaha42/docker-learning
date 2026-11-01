#Connecting Flask app to MySQL database

from flask import Flask #creating new flask application instance
import MySQLdb #enables us to execute sql commands within our python app


app = Flask(__name__) #app is a variable

@app.route('/') #defining route url
def hello_world():
    # Establishing connection to the MySQL database
    db = MySQLdb.connect(
        host="mydb",    # Hostname of the MySQL container
        user="root",    # Username to connect to MySQL
        passwd="my-secret-pw",  # Password for the MySQL user
        db="mysql"      # Name of the database to connect to
    )
    #Doing a simple query to find the MySQL version
    cur = db.cursor()
    cur.execute("SELECT VERSION()")
    version = cur.fetchone()
    return f'Hello, World! MySQL version: {version[0]}'

if  __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002) #tell the variable "app" to run on our local host 0.0.0.0 on port 5000 - allows us to look on localhost5000 for this app