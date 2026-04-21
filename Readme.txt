☀️ Solar Power Monitoring System
-------------------------------------------------------------------------------------------------------------------------------------------
📌 Overview
-------------------------------------------------------------------------------------------------------------------------------------------
This project is a **real-time solar power monitoring application** that simulates solar panel data, streams it using Kafka, processes it using Pandas, stores it in a SQL database, and visualizes it through an interactive Streamlit dashboard.

-------------------------------------------------------------------------------------------------------------------------------------------
⚙️ Tech Stack
-------------------------------------------------------------------------------------------------------------------------------------------
* **Python** – Core programming
* **Apache Kafka** – Real-time data streaming
* **Pandas** – Data processing
* **SQLite** – Database storage
* **Streamlit** – User Interface (Dashboard)
* **Docker** – Kafka infrastructure
-------------------------------------------------------------------------------------------------------------------------------------------
🏗️ Architecture
-------------------------------------------------------------------------------------------------------------------------------------------
Sensor Simulator → Kafka Producer → Kafka Topic → Consumer → SQLite DB → Streamlit UI
-------------------------------------------------------------------------------------------------------------------------------------------
📁 Project Structure
-------------------------------------------------------------------------------------------------------------------------------------------
solar_project/
│
├── scripts/
│   ├── sensor_simulator.py
│   ├── kafka_producer.py
│   ├── kafka_consumer.py
│   ├── db_loader.py
│
├── dashboard/
│   └── app.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── start.sh
├── wait-for-kafka.sh
-------------------------------------------------------------------------------------------------------------------------------------------
🚀 Setup & Execution (Using Virtual Environment)
-------------------------------------------------------------------------------------------------------------------------------------------
 🔹 Step 1: Clone Repository


		git clone <your-repo-url>
		cd solar_project



🔹 Step 2: Create Virtual Environment

		python -m venv venv


🔹 Step 3: Activate Virtual Environment

			For PowerShell:

					venv\Scripts\activate.bat


🔹 Step 4: Install Dependencies


			pip install kafka-python pandas streamlit

-------------------------------------------------------------------------------------------------------------------------------------------
🐳 Start Kafka (Docker Required)
-------------------------------------------------------------------------------------------------------------------------------------------
			Start Kafka & Zookeeper:

			docker-compose up -d
			 Verify:
					docker ps


			 Create Kafka Topic (one-time)

					docker exec -it solar_project-kafka-1 kafka-topics.sh ^ --create --topic solar_topic ^ --bootstrap-server localhost:9092  --partitions 1 --replication-factor 1
-------------------------------------------------------------------------------------------------------------------------------------------
▶️ Run the Application
-------------------------------------------------------------------------------------------------------------------------------------------
	🔹 Step 1: Run Producer (Terminal 1)
						python scripts\kafka_producer.py

	🔹 Step 2: Run Consumer (Terminal 2)

						venv\Scripts\activate.bat
						python scripts\kafka_consumer.py

	🔹 Step 3: Run Dashboard (Terminal 3)

						venv\Scripts\activate.bat
						streamlit run dashboard\app.py
-------------------------------------------------------------------------------------------------------------------------------------------
🌐 Access Dashboard
-------------------------------------------------------------------------------------------------------------------------------------------
			Open in browser: http://localhost:8501


			 📊 Features

				* Real-time solar data simulation
				* Kafka-based streaming pipeline
				* Data processing with Pandas
				* SQLite database storage
				* Live dashboard with charts
				* Auto-refresh UI
-------------------------------------------------------------------------------------------------------------------------------------------
 🔴 Common Issues & Fixes
-------------------------------------------------------------------------------------------------------------------------------------------
	 ❌ NoBrokersAvailable

	✔ Ensure Kafka is running
	✔ Use: bootstrap_servers="localhost:9092"

	 ❌ No table found

	✔ Run **consumer first**

	 ❌ No data in UI

	✔ Ensure both producer and consumer are running

-------------------------------------------------------------------------------------------------------------------------------------------
🧠 Key Concepts
-------------------------------------------------------------------------------------------------------------------------------------------
* **Streaming Pipeline** (Kafka)
* **ETL Process** (Extract → Transform → Load)
* **Real-time Data Simulation**
* **Dashboard Visualization**
-------------------------------------------------------------------------------------------------------------------------------------------
🎯 How It Works
-------------------------------------------------------------------------------------------------------------------------------------------
1. Sensor simulator generates data
2. Producer sends data to Kafka
3. Consumer processes and stores data in SQLite
4. Streamlit fetches and displays data
-------------------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------------
👨‍💻 Author
-------------------------------------------------------------------------------------------------------------------------------------------
**Ayush Singh**

-------------------------------------------------------------------------------------------------------------------------------------------

⭐ Future Enhancements
-------------------------------------------------------------------------------------------------------------------------------------------
* Alert system (high temperature warning)
* Cloud deployment (AWS)
* Advanced analytics
* Machine learning for prediction
-------------------------------------------------------------------------------------------------------------------------------------------
📌 One-Line Summary
-------------------------------------------------------------------------------------------------------------------------------------------
> A real-time solar monitoring system using Kafka, Pandas, SQLite, and Streamlit with a live dashboard.

