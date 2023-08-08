import psycopg2


def get_connection():
    return psycopg2.connect("dbname='postgres' user='postgres' host='db' password='password'")


def set_up_db(connection):
    with connection.cursor() as c:
        c.execute("""
        CREATE TABLE IF NOT EXISTS sreality (
	        ad_name VARCHAR (255),
	        img_url TEXT );
        """)

def insert_ad(ad_name, image_url, connection):
    with connection.cursor() as c:
        c.execute(f"INSERT INTO sreality (ad_name, img_url) VALUES ('{ad_name}', '{image_url}');")


def read_ads(connection):
    with connection.cursor() as c:
        c.execute("SELECT * FROM sreality;")
        return c.fetchall()
