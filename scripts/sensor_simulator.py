import random
from datetime import datetime

def generate_data():
    return {
        "timestamp": str(datetime.now()),
        "panel_id": random.randint(1, 5),
        "power_kw": round(random.uniform(5, 50), 2),
        "temperature_c": round(random.uniform(20, 70), 2)
    }
