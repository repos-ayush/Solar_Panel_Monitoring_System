#!/bin/bash
./wait-for-kafka.sh
python scripts/kafka_producer.py &
python scripts/kafka_consumer.py &
wait
