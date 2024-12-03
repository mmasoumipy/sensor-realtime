import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# load environment variables
load_dotenv()

# create a connection to the database
engine = create_engine(
    f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
)

def get_latest_data():
    """ 
    Retrieve the latest 50 sensor readings from the database.

    :return: DataFrame containing the latest sensor readings
    """
    query = "SELECT * FROM sensor_readings ORDER BY timestamp DESC LIMIT 50"
    data = pd.read_sql(query, engine)
    return data

def calculate_aggregations(data):
    """
    Calculate average, max, and min values for temperature, humidity, and pressure

    :param data: DataFrame containing sensor readings
    :return: Dictionary containing the aggregations
    """
    aggregations = {
        "temperature": {
            "average": data["temperature"].mean(),
            "max": data["temperature"].max(),
            "min": data["temperature"].min(),
        },
        "humidity": {
            "average": data["humidity"].mean(),
            "max": data["humidity"].max(),
            "min": data["humidity"].min(),
        },
        "pressure": {
            "average": data["pressure"].mean(),
            "max": data["pressure"].max(),
            "min": data["pressure"].min(),
        },
    }
    return aggregations

def detect_anomalies(data):
    """
    Detect anomalies in the sensor readings

    :param data: DataFrame containing sensor readings
    :return: DataFrame containing the anomalies
    """
    anomalies = data[
        (data["temperature"] > 40) | 
        (data["pressure"] < 950)
    ]
    return anomalies

def main():
    """
    Main function to fetch latest data, calculate aggregations, and detect anomalies.
    """
    print("Fetching latest data...")
    data = get_latest_data()
    print(f"Fetched {len(data)} records.")

    print("\nCalculating aggregations...")
    aggregations = calculate_aggregations(data)
    for metric, stats in aggregations.items():
        print(f"\n{metric.capitalize()}:")
        print(f"  Average: {stats['average']:.2f}")
        print(f"  Max: {stats['max']:.2f}")
        print(f"  Min: {stats['min']:.2f}")

    print("\nDetecting anomalies...")
    anomalies = detect_anomalies(data)
    if not anomalies.empty:
        print("Anomalies detected:")
        print(anomalies)
    else:
        print("No anomalies detected.")


if __name__ == "__main__":
    main()
