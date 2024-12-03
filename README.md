# Sensor Realtime Streaming Dashboard 🌡️📊

This project is a **real-time streaming dashboard** for monitoring and analyzing sensor data, implemented using **Python**, **Streamlit**, and **MySQL**. The system includes components for data generation, processing, and visualization, offering insights like statistical aggregations, anomaly detection, and trend visualization.



## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Project Structure](#project-structure)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Environment Variables](#environment-variables)
7. [Technologies Used](#technologies-used)
8. [Future Enhancements](#future-enhancements)



## Overview

The **Sensor Realtime Streaming Dashboard** simulates a data pipeline where:
- Sensor readings (temperature, humidity, and pressure) are generated randomly.
- Data is stored in a MySQL database.
- A Streamlit dashboard visualizes data trends and detects anomalies.

The dashboard auto-refreshes every 10 seconds to display real-time updates.



## Features

1. **Real-time Data Simulation:**
   - Randomly generated sensor data (10 sensors).
   - Inserts data into the database every 2 seconds.

2. **Streamlit Dashboard:**
   - Displays recent sensor readings.
   - Shows statistical aggregations (average, max, min).
   - Detects anomalies based on predefined conditions.
   - Provides visualization of trends for temperature and humidity.
   - Filters data by specific sensors.

3. **Data Processing:**
   - Extracts and processes sensor data from the database.
   - Calculates aggregations and identifies anomalies.



## Project Structure

```
sensor_realtime/
│
├── README.md             # Project documentation
├── requirements.txt      # Dependencies
├── .env                  # Environment variables
│
├── src/                  # Source code
│   ├── producer/         # Data generation module
│   │   ├── data_producer.py
│   │   └── __init__.py
│   │
│   ├── processor/        # Data processing module
│   │   ├── data_processor.py
│   │   └── __init__.py
│   │
│   ├── dashboard/        # Streamlit dashboard
│       └── app.py
```



## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/sensor-realtime-dashboard.git
   cd sensor-realtime
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database:
   - Install MySQL and create a database.
   - Configure environment variables in the `.env` file.

4. Run the data producer to simulate sensor data:
   ```bash
   python src/producer/data_producer.py
   ```

5. Start the Streamlit dashboard:
   ```bash
   streamlit run src/dashboard/app.py
   ```



## Usage

- The **data producer** generates sensor data and stores it in the MySQL database.
- The **Streamlit dashboard** fetches and visualizes the data, allowing you to:
  - View the most recent 100 sensor readings.
  - Analyze statistics and trends.
  - Detect anomalies in sensor readings.



## Environment Variables

Create a `.env` file in the root directory with the following entries:

```plaintext
DB_HOST=your-database-host
DB_USER=your-database-username
DB_PASSWORD=your-database-password
DB_NAME=your-database-name
```



## Technologies Used

- **Python**
- **Streamlit**: Real-time data visualization.
- **MySQL**: Database for sensor data storage.
- **SQLAlchemy**: ORM for database interaction.
- **pandas**: Data manipulation and analysis.
- **dotenv**: Environment variable management.



## Future Enhancements

- Add support for Kafka for distributed streaming.
- Extend the dashboard to include more sensor metrics.
- Implement authentication for the dashboard.
- Store processed data in a NoSQL database for scalability.
