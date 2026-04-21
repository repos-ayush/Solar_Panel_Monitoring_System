FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y netcat-openbsd
RUN chmod +x start.sh wait-for-kafka.sh
CMD ["sh", "-c", "./start.sh & streamlit run dashboard/app.py --server.port 8501 --server.address 0.0.0.0"]
