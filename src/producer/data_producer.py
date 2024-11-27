import pymysql as mysql
import random
import time
from dotenv import load_dotenv
import os


load_dotenv()


db = mysql.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)
cursor = db.cursor()


create_table_query = """
CREATE TABLE IF NOT EXISTS sensor_readings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sensor_id INT NOT NULL,
    temperature FLOAT NOT NULL,
    humidity FLOAT NOT NULL,
    pressure FLOAT NOT NULL,
    timestamp DATETIME NOT NULL
);
"""
cursor.execute(create_table_query)
db.commit()


while True:
    sensor_id = random.randint(1, 10)
    temperature = round(random.uniform(-40.0, 50.0), 2) 
    humidity = round(random.uniform(30.0, 70.0), 2)
    pressure = round(random.uniform(500.0, 1100.0), 2)
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

    query = """
    INSERT INTO sensor_readings (sensor_id, temperature, humidity, pressure, timestamp)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (sensor_id, temperature, humidity, pressure, timestamp))
    db.commit()
    print(f"Inserted: Sensor {sensor_id}, Temp: {temperature}, Humidity: {humidity}, Pressure: {pressure}, Time: {timestamp}")
    time.sleep(2)
