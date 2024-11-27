import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# بارگذاری تنظیمات از فایل .env
load_dotenv()

# اتصال به دیتابیس
engine = create_engine(
    f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
)


def get_latest_data():
    """
    دریافت داده‌های اخیر از دیتابیس
    """
    query = "SELECT * FROM sensor_readings ORDER BY timestamp DESC LIMIT 50"
    data = pd.read_sql(query, engine)
    return data

def calculate_aggregations(data):
    """
    محاسبه تجمیع‌های آماری مثل میانگین، حداکثر و حداقل
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
    شناسایی مقادیر غیرعادی در داده‌ها (مثلاً دمای بالای 40 یا فشار زیر 950)
    """
    anomalies = data[
        (data["temperature"] > 40) | 
        (data["pressure"] < 950)
    ]
    return anomalies

def main():
    """
    عملیات اصلی پردازش داده‌ها
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
