import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()


engine = create_engine(
    f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
)

# Fetch data from the database
def fetch_data():
    query = "SELECT * FROM sensor_readings ORDER BY timestamp DESC LIMIT 100"
    data = pd.read_sql(query, engine)
    return data

# Calculate aggregations -- average, max, min
def calculate_aggregations(data):
    aggregations = {
        "Temperature": {
            "Average": data["temperature"].mean(),
            "Max": data["temperature"].max(),
            "Min": data["temperature"].min(),
        },
        "Humidity": {
            "Average": data["humidity"].mean(),
            "Max": data["humidity"].max(),
            "Min": data["humidity"].min(),
        },
        "Pressure": {
            "Average": data["pressure"].mean(),
            "Max": data["pressure"].max(),
            "Min": data["pressure"].min(),
        },
    }
    return pd.DataFrame(aggregations)

# Detect anomalies -- temperature > 40 or pressure < 950
def detect_anomalies(data):
    anomalies = data[
        (data["temperature"] > 40) | 
        (data["pressure"] < 950)
    ]
    return anomalies


st.title("Sensor Data Streaming Dashboard")

# Fetch and display the latest sensor readings
st.subheader("Recent Sensor Readings")
data = fetch_data()
st.dataframe(data)

# Display aggregations
st.subheader("Aggregations (Statistics)")
aggregations = calculate_aggregations(data)
st.dataframe(aggregations)

# Display temperature and humidity trends
st.subheader("Temperature and Humidity Trends")
st.line_chart(data[["temperature", "humidity"]])

# Display anomalies
st.subheader("Anomalies Detection")
anomalies = detect_anomalies(data)
if anomalies.empty:
    st.success("No anomalies detected.")
else:
    st.warning("Anomalies detected!")
    st.dataframe(anomalies)

# Display data for a specific sensor -- select sensor ID
sensor_id = st.selectbox("Select Sensor ID", sorted(data["sensor_id"].unique()))
filtered_data = data[data["sensor_id"] == int(sensor_id)]
st.subheader(f"Data for Sensor {sensor_id}")
st.dataframe(filtered_data)


