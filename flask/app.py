import psycopg2
from flask import Flask, render_template


def get_connection():
    return psycopg2.connect("dbname='postgres' user='postgres' host='db' password='password'")


def read_ads(connection):
    with connection.cursor() as c:
        c.execute("SELECT * FROM sreality;")
        return c.fetchall()
    connection.close()


application = Flask(__name__)



@application.route("/")
def index():
    return render_template("index.html", estates=read_ads(get_connection()))


if __name__ == "__main__":
    application.run(host="0.0.0.0", port=8080)