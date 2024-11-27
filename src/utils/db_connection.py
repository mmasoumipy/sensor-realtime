import pymysql as mysql
from dotenv import load_dotenv
import os

load_dotenv()

def get_db_connection():
    return mysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
