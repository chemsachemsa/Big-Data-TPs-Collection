import csv
import random
import string
import os

filename = "big_dataset.csv"

rows_per_chunk = 100000
target_size = 5 * 1024 * 1024 * 1024   # 5GB

header = ["id", "device_name", "temperature", "humidity", "status"]

def random_string(length=10):
    return ''.join(random.choices(string.ascii_letters, k=length))

with open(filename, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)

    while os.path.getsize(filename) < target_size:
        for _ in range(rows_per_chunk):
            row = [
                random.randint(1, 10000000),
                random_string(),
                round(random.uniform(10, 40), 2),
                round(random.uniform(30, 90), 2),
                random.choice(["ON", "OFF"])
            ]
            writer.writerow(row)

print("Dataset generated successfully")
print("Size:", os.path.getsize(filename) / (1024**3), "GB")