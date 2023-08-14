import scrapy
import json
import unicodedata

import psycopg2
from psycopg2 import sql


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
        c.execute(sql.SQL("INSERT INTO {} (ad_name, img_url) VALUES (%s, %s);").format(sql.Identifier('sreality')), [ad_name, image_url])


class SrealitySpider(scrapy.Spider):
    name = "sreality"

    def start_requests(self):
        urls = [
            "https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&page=1&per_page=500",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        estates = json.loads(response.text)["_embedded"]["estates"]
        db_connection = get_connection()
        set_up_db(db_connection)
        for estate in estates:
            estate_name = unicodedata.normalize('NFKD', estate['name'])
            estate_image = estate['_links']['images'][0]["href"]
            insert_ad(estate_name, estate_image, db_connection)

        db_connection.commit()
        db_connection.close()
